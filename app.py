import flask
import matplotlib.pyplot as plt
import io # input / output
import pandas as pd
import geopandas as gpd

app = flask.Flask("Do you know your city?")

# DYNAMIC
@app.route("/")
def home():
    return flask.render_template('index.html')
    # with open('index.html') as f:
    #     return f.read()
    
@app.route("/script.js")
def js():
    with open('script.js') as f:
        return f.read()
 
if __name__ == "__main__":
    # threaded must be False whenever we use matplotlib
    app.run(host="0.0.0.0", debug=True, threaded=False, port=8080)
