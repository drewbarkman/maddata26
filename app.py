import flask
import matplotlib
import io # input / output
import pandas as pd
import geopandas as gpd
import numpy as np

app = flask.Flask("Do you know your city?")

# Making map
city_limits = gpd.read_file('City_Limit.geojson')
water = gpd.read_file("Lakes_and_Rivers.geojson").to_crs(city_limits.crs)
streets = gpd.read_file("Street_Centerlines_and_Pavement_Data.geojson").to_crs(city_limits.crs)
place_coords = np.array([-89.4070977, 43.0680178])

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

matplotlib.pyplot.close()

# Score tracker
longest_streak = 0
current_streak = 0
current_score = 0

# DYNAMIC
@app.route("/")
def home():
    # with open("index.html") as f:
    #     html = f.read()

    # mode = flask.request.args.get('mode')
    return flask.render_template('index.html')

@app.route('/data')
def send_data():
    mode = flask.request.args.get('mode')
    print(mode)
    test_data = {'name': 'hiiii', 'mode': mode}
    return flask.jsonify(test_data)

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
