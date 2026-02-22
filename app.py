import flask
import matplotlib
import io # input / output
import pandas as pd
import geopandas as gpd
import numpy as np
import function

app = flask.Flask("Do you know your city?")

# Making map VVV Change this to whatever place is chosen VVV


# DYNAMIC
@app.route("/")
def home():
    return flask.render_template('index.html')

@app.route('/data', methods = ["GET", "POST"])
def send_data():
    mode = flask.request.form.get('mode')
    area = flask.request.form.get('area')
    print(mode, area)
    test_data = {'mode': mode, 'area': area}
    place = function.choose_place(mode, area)
    print(place)
    reviews = function.get_reviews(place)
    global coords 
    coords = reviews['coords']
    print(coords)
    print(reviews)

    options = []
    while len(options) < 4: 
        chosen_place = function.choose_place(mode, area)['name']
        print(chosen_place)
        if chosen_place in options:
            continue
        options.append(chosen_place)
    
    reviews['options'] = options

    return flask.jsonify(reviews)

@app.route("/map.svg")
def map():
    city_limits = gpd.read_file('City_Limit.geojson')
    water = gpd.read_file("Lakes_and_Rivers.geojson").to_crs(city_limits.crs)
    streets = gpd.read_file("Street_Centerlines_and_Pavement_Data.geojson").to_crs(city_limits.crs)

    f = function.map(coords, city_limits, water, streets)
    return f.getvalue()

@app.route("/script.js")
def js():
    with open('script.js') as f:
        return f.read()

if __name__ == "__main__":
    # threaded must be False whenever we use matplotlib
    app.run(host="0.0.0.0", debug=True, threaded=False, port = 8080)
