from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import yaml
import json
import requests
import sqlite3
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

database = 'database.db'

config = yaml.safe_load(open('config.yml'))
lat = config['lat']
lon = config['lon']
openweather_api_key = config['openweather_api_key']

def setup_db():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    query = 'CREATE TABLE IF NOT EXISTS todo (text TEXT, date DATE)'
    print("executing: ", query)
    cursor.execute(query)



@app.route('/weather')
def weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}&units=metric&lang=de"
    response = requests.get(url)
    data = json.loads(response.text)

    res = {}
    res['description'] = data['weather'][0]['description']
    res['temperature'] = data['main']['temp']

    return res

@app.route('/todos/today')
def todos_today():
    today = datetime.today().strftime('%Y-%m-%d')

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    query = f'SELECT (text) FROM todo WHERE date = "{today}"'
    cursor.execute(query)

    res = list(map(lambda e: e[0], list(cursor.fetchall())))
    print(res)

    return res

@app.route('/todos', methods=['POST'])
def post_todo():
    text = request.json['text']
    date = request.json['date']

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        query = f'INSERT INTO todo (text, date) VALUES ("{text}", "{date}")'
        cursor.execute(query)
        connection.commit()
    except:
        return {'success': False}
    return {'success': True}

if __name__ == '__main__':
    setup_db()
    app.run(host="0.0.0.0", debug=True)
