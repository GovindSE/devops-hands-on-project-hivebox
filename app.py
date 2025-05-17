from flask import Flask, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/sensors")
def get_sensor_data():
    sensebox_ids = os.getenv("SENSEBOX_IDS", "").split(",")
    data = {}
    for box_id in sensebox_ids:
        url = f"https://api.opensensemap.org/boxes/{box_id}"
        res = requests.get(url)
        if res.status_code == 200:
            data[box_id] = res.json()
        else:
            data[box_id] = {"error": "Could not fetch data"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

