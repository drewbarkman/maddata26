import numpy as np
import matplotlib
import io
import ast
import pandas as pd
from time import sleep

reviews_df = pd.read_csv("testing_reviews.csv")

def map(place_coords, city_limits, water, streets):
    rand_num = np.random.rand(2)
    while np.sqrt(rand_num[0]**2 + rand_num[1]**2) > 1:
        # print('trying again')
        rand_num = rand_num = np.random.rand(2)
    rand_num[0] = (rand_num[0] - 0.5) / 54.6 / 2
    rand_num[1] = (rand_num[1] - 0.5) / 69 / 2
    area_center = place_coords - rand_num
    ax = city_limits.plot(color="tan", alpha= 0.6)
    water.plot(color="lightblue", ax=ax)
    streets.plot(color="gray", ax=ax, alpha=1)
    ax.set_axis_off()
    # ax.plot(place_coords[0], place_coords[1], marker='o', alpha=0.5)
    ax.add_patch(matplotlib.patches.Ellipse((area_center[0], area_center[1]), width = 0.6 / 52, height = 0.6 / 69,
                            edgecolor='red', facecolor='salmon', linewidth=0.5))
    ax.set_xlim(area_center[0] - 0.025,
                area_center[0] + 0.025)
    ax.set_ylim(area_center[1] - 0.02,
                area_center[1] + 0.02)

    try:
        f = io.StringIO()
        matplotlib.pyplot.savefig(f, format="svg", bbox_inches='tight')  
        print("SVG file saved successfully as f")
    except Exception as e:
        print(f"Error saving SVG: {e}")
    # matplotlib.pyplot.savefig('map.svg', format="svg", bbox_inches='tight') 

    matplotlib.pyplot.close()
    # pass
    return f

def choose_place(our_type, area):
    place = reviews_df.iloc[int(np.random.rand() * len(reviews_df))]
    
    types = ast.literal_eval(place['our_type'])
    areas = ast.literal_eval(place['our_area'])
    non_empty = ast.literal_eval(place['cleaned_reviews'])
    count = 0
    for review in ast.literal_eval(place['cleaned_reviews'])[0]:
        if type(review['text']) == str:
            count += 1
    if our_type == 'all':
        if area == 'all':
            while count < 2:
                place = reviews_df.iloc[int(np.random.rand() * len(reviews_df))]
                types = ast.literal_eval(place['our_type'])
                areas = ast.literal_eval(place['our_area'])
                count = 0
                for review in ast.literal_eval(place['cleaned_reviews'])[0]:
                    if type(review['text']) == str:
                        count += 1
        else:
            while (not area in areas) or (count < 2):
                place = reviews_df.iloc[int(np.random.rand() * len(reviews_df))]
                types = ast.literal_eval(place['our_type'])
                areas = ast.literal_eval(place['our_area'])
                count = 0
                for review in ast.literal_eval(place['cleaned_reviews'])[0]:
                    if type(review['text']) == str:
                        count += 1
    else:
        if area == 'all':
            while (not our_type in types) or (count < 2):
                place = reviews_df.iloc[int(np.random.rand() * len(reviews_df))]
                types = ast.literal_eval(place['our_type'])
                areas = ast.literal_eval(place['our_area'])
                count = 0
                for review in ast.literal_eval(place['cleaned_reviews'])[0]:
                    if type(review['text']) == str:
                        count += 1
        else:
            while (not (our_type in types and area in areas)) or (count < 2):
                # print(types)
                # print(our_type in types)
                # print(areas)
                # print(area in areas)
                # print(count)
                # print((not (our_type in types and not area in areas)) or (count < 2))
                # sleep(3)
                place = reviews_df.iloc[int(np.random.rand() * len(reviews_df))]
                types = ast.literal_eval(place['our_type'])
                areas = ast.literal_eval(place['our_area'])
                count = 0
                for review in ast.literal_eval(place['cleaned_reviews'])[0]:
                    if type(review['text']) == str:
                        count += 1
    return place

def get_reviews(place):
    place_reviews = ast.literal_eval(place['cleaned_reviews'])
    place_reviews_df = pd.DataFrame(place_reviews[0])
    place_reviews_df = place_reviews_df[~(place_reviews_df['text'].isna())]

    if place_reviews_df.rating.min() == place_reviews_df.rating.max():
        positives = place_reviews_df[place_reviews_df['rating'] == place_reviews_df.rating.max()]
        rand_num = int(np.random.rand() * len(positives))
        rand_positive = positives.iloc[rand_num]
        rand_negative = positives.iloc[(rand_num + 1) % len(positives)]

    else:
        positives = place_reviews_df[place_reviews_df['rating'] == place_reviews_df.rating.max()]
        rand_positive = positives.iloc[int(np.random.rand() * len(positives))]

        negatives = place_reviews_df[place_reviews_df['rating'] == place_reviews_df.rating.min()]
        rand_negative = negatives.iloc[int(np.random.rand() * len(negatives))]

        answer = place['name']

        coords = [place['long'], place['lat']]

        url = place['url']

        return {'positive_rating': rand_positive.to_dict()['rating'], "positive_text": rand_positive.to_dict()['text'], 
                'negative_rating': rand_negative.to_dict()['rating'], 'negative_text': rand_negative.to_dict()['text'], 
                'answer': answer, 'coords': coords, 'url': url}