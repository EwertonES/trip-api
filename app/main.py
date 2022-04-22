import os
from flask import Flask
from flask import request
from google.cloud import bigquery
import geojson

class MyPoint():
    def __init__(self, x):
        self.x, self.y = map(float, x.replace("POINT (", "").replace(")", "").split(" "))

    @property
    def __geo_interface__(self):
        return {'type': 'Point', 'coordinates': (self.x, self.y)}

app = Flask(__name__)

@app.route("/trip", methods=["POST"])
def trip():
    """Uploads schema-compatible JSON to Big Query"""
    content = request.get_json()
    for col in ["origin_coord", "destination_coord"]:
        try:
            content[col] = geojson.dumps(MyPoint(content[col]))
        except (KeyError, ValueError, AttributeError) as e:
            return "invalid input, object invalid", 400
    
    errors = bigquery.Client().insert_rows_json("ewerton-jobsity.jobsity.trips", [content])
    if errors:
        return "invalid input, object invalid", 400

    return "trip created", 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False, port=int(os.environ.get("PORT", 8080)))
