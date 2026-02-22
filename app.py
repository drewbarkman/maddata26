import flask
import matplotlib
import io # input / output
import pandas as pd
import geopandas as gpd
import numpy as np
import function

app = flask.Flask("Do you know your city?")

# Making map
place_coords = np.array([-89.4070977, 43.0680178])
city_limits = gpd.read_file('City_Limit.geojson')
water = gpd.read_file("Lakes_and_Rivers.geojson").to_crs(city_limits.crs)
streets = gpd.read_file("Street_Centerlines_and_Pavement_Data.geojson").to_crs(city_limits.crs)
place_coords = np.array([-89.4070977, 43.0680178])

f = function.map(place_coords, city_limits, water, streets)

# Score tracker
longest_streak = 0
current_streak = 0
current_score = 0

# DYNAMIC
@app.route("/")
def home():
    return flask.render_template('index.html')

@app.route("/map.svg")
def map():
    return f.getvalue()

@app.route("/script.js")
def js():
    with open('script.js') as f:
        return f.read()

if __name__ == "__main__":
    # threaded must be False whenever we use matplotlib
    app.run(host="0.0.0.0", debug=True, threaded=False, port = 8080)
