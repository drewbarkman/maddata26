import googlemaps
import os
import time
import requests
from dotenv import load_dotenv
import pandas as pd
import geopandas as gpd
import re
import matplotlib.pyplot as plt
import numpy as np
from better_profanity import profanity
import ast
load_dotenv()

def select_first_two_words(name):
    split_name = name.lower().split(' ')
    i = -1
    final_name = []
    while len(final_name) < 2:
        i += 1
        try:
            if split_name[i] == 'the' or split_name[i] == 'madison' or split_name[i] == '-':
                continue
            else:
                split_name[i] = split_name[i].replace(",", "").replace("’", "'").replace("à", "a").replace("è", "e")
                final_name.append(split_name[i])
        except IndexError:
            break
            
    final_name = " ".join(final_name)
    return final_name

def censor_review(place_name, review):
    cleaned_review = ""

    # censor common swear words
    profanity.load_censor_words()
    cleaned_review = profanity.censor(review)

    # in reviews we have read today, we've seen these words commonly used in a negative connotation
    custom_swear_list = ['hispanic', 'black', 'latino', 'english', 'spanish', 'asian']
    profanity.add_censor_words(custom_swear_list)
    if profanity.contains_profanity(cleaned_review):
        # completely remove review if it is derogatory
        return None
    
    for word in place_name.split(" "):
        search_string = "(?i)" + word
        if cleaned_review == "":
            cleaned_review = re.sub(search_string, '*****', review)
        else:
            cleaned_review = re.sub(search_string, '*****', cleaned_review)
        word = word.replace("'", "").replace(".", "").replace("\n", "")
        search_string = "(?i)" + word
        cleaned_review = re.sub(search_string, '*****', cleaned_review)
    return cleaned_review

def clean_reviews(row):
    cleaned_review_list = []
    for review in row['reviews']:
        cleaned_review = {
            'rating': review['rating'],
            'text': censor_review(row['shortened_name'], review['text'])
        }
        cleaned_review_list.append(cleaned_review)

    return [cleaned_review_list]

maps_client = googlemaps.Client(key = os.getenv('google_maps_api_key'))

place_types = ['restaurant', 'bar', 'cafe', 'fastfood']
restaurant_list = []
bar_list = []
cafe_list = []
type_lists = [restaurant_list, bar_list, cafe_list]

results = []

area = ['downtown madison, wisconsin', 'westside madison, wisconsin', 'eastside madison, wisconsin']

place_ids = set()

for k in range(len(area)):
    for j in range(len(place_types)):
        for i in range(0, 2):
            if i == 0:
                response = maps_client.places(f"{place_types[j]} in {area[k]}", type = [place_types[j]])

            else:
                response = maps_client.places(f"{place_types[j]} in {area[k]}", type = [place_types[j]], page_token = next_page_token)
            
            
            for place in response['results']:
                if place['place_id'] in place_ids:
                    for establishment in results:
                        if place['place_id'] == establishment['place_id']:
                            establishment['our_type'].append(place_types[j])
                            establishment['our_area'].append(area[k])
                            break
                    
                        else:   
                            continue
                else:
                    place_ids.add(place['place_id'])
                    place['our_type'] = [place_types[j]]
                    place['our_area'] = [area[k]]
                    results.append(place)
                    
            try:
                next_page_token = response['next_page_token']
            except KeyError:
                continue
            # We look for a next page token even when we aren't going to the next page
            time.sleep(2)


places = []

df = gpd.GeoDataFrame.from_dict(places)

df['shortened_name'] = df['name'].apply(select_first_two_words)
df['cleaned_reviews'] = df.apply(clean_reviews, axis = 1)

df.to_csv('reviews.csv')