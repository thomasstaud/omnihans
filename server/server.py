from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import yaml
import json
import requests

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

config = yaml.safe_load(open('config.yml'))
lat = config['lat']
lon = config['lon']
openweather_api_key = config['openweather_api_key']

@app.route('/weather')
def weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}&units=metric&lang=de"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)

    res = {}
    res['description'] = data['weather'][0]['description']
    res['temperature'] = data['main']['temp']

    return res

if __name__ == '__main__':
    app.run(debug=True)
