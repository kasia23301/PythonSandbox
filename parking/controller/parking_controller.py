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


@app.route('/parking', methods=['POST'])  # obsługuje zadania POST - czyli takie które coś dodają np. nowy parking
def wstawianie_danych():
    data = request.data  # request to zapytanie wysłane do serwera - jest w nim wiele rzeczy, ale nas insteresuje tylko data (czyli to co wysyłasz w postmanie jako body przy pomocy POST)
    dataDict = json.loads(data)  # teraz zaminiamy json'a z requestu na słownik
    id = dataDict["id"]  # pobranie wartości dla klucza "id" ze słownika
    name = dataDict["name"]
    attitude = dataDict["attitude"]
    longitude = dataDict["longitude"]
    free_spaces = dataDict["free_spaces"]
    capacity = dataDict["free_spaces"]
    rating = dataDict["rating"]
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingDB'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = '''insert into Parking(id,name,attitude,longitude,free_spaces,capacity,rating) 
    values(%s,%s,%s,%s,%s,%s,%s)'''
    conn.commit()
    cursor.execute(_SQL, ('NULL', 'Warszawia', '18.490', '27.765', '12', '130, 5'))
    return jsonify(dataDict), 200  # zwrócenie jsona (powstałego ze słownika po użyciu funkcji jsonify) i statusu 200 (oznancza on, że wszytsko poszło ok)
    cursor.close()
    conn.close()

#@app.route('/parking')
#def usuwanie_danych():
    #dbconfig = {'host': '127.0.0.1',
                #'user': 'root',
                #'password': 'arogontaldo',
                #'database': 'parkingDB'}
    #conn = mysql.connector.connect(**dbconfig)
    #_SQL = '''DELETE FROM Parking WHERE id=2'''
    #cursor = conn.cursor()
    #cursor.execute(_SQL)


if __name__ == "__main__":
    app.run(debug=True)
