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

# rewrite todos to be a rest service?
# practice + need all of get, post, put, delete anyway

def setup_db():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    query = 'CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, text TEXT, date DATE, checked BOOL)'
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
    query = f'SELECT id, text, date, checked FROM todo WHERE date = "{today}"'
    cursor.execute(query)

    res = list(map(lambda e: {'id': e[0], 'text': e[1], 'date': e[2], 'checked': bool(e[3])}, list(cursor.fetchall())))
    print(res)

    return res

@app.route('/todos/not-today')
def todos_not_today():
    today = datetime.today().strftime('%Y-%m-%d')

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    query = f'SELECT id, text, date, checked FROM todo WHERE date != "{today}"'
    cursor.execute(query)

    res = list(map(lambda e: {'id': e[0], 'text': e[1], 'date': e[2], 'checked': bool(e[3])}, list(cursor.fetchall())))
    print(res)

    return res

@app.route('/todos', methods=['POST'])
def post_todo():
    text = request.json['text']
    date = request.json['date']
    checked = False

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        query = f'INSERT INTO todo (text, date, checked) VALUES ("{text}", "{date}", {checked})'
        cursor.execute(query)
        connection.commit()
    except:
        return {'success': False}
    return {'success': True}

@app.route('/todos', methods=['PUT'])
def put_todo():
    id = request.json['id']
    text = request.json['text']
    date = request.json['date']
    checked = request.json['checked']

    print(checked)

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        query = f'UPDATE todo SET text="{text}", date="{date}", checked={checked} WHERE id={id}'
        cursor.execute(query)
        connection.commit()
    except:
        return {'success': False}
    return {'success': True}


if __name__ == '__main__':
    setup_db()
    app.run(host="0.0.0.0", debug=True)
