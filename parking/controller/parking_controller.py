from flask import Flask, jsonify, request
import mysql.connector
import json

app = Flask(__name__)


@app.route('/parking')
def wczytywanie_danych():
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingDB'}
    conn = mysql.connector.connect(**dbconfig)
    _SQL = '''select id, name, attitude, longitude, free_spaces, capacity, rating from parking'''
    cursor = conn.cursor()
    cursor.execute(_SQL)
    lista = []
    for wiersz in cursor.fetchall():
        slownik = {}
        slownik["id"] = wiersz[0]
        slownik["name"] = wiersz[1]
        slownik["attitude"] = wiersz[2]
        slownik["longitude"] = wiersz[3]
        slownik["free_spaces"] = wiersz[4]
        slownik["capacity"] = wiersz[5]
        slownik["rating"] = wiersz[6]
        lista.append(slownik)
    cursor.close()
    return jsonify(lista), 200


@app.route('/parking', methods=['POST'])
def wstawianie_danych():
    id = request.id
    name = request.name
    attitude = request.attitude
    longitude = request.longitude
    free_spaces = request.free_spaces
    capacity = request.capacity
    rating = request.rating
    _SQL = '''insert id, name, attitude, longitude, free_spaces, capacity, rating from parking'''
    data = request.data
    dataDict = json.loads(data)
    print(dataDict)
    return jsonify(dataDict), 200


if __name__ == "__main__":
    app.run(debug=True)
