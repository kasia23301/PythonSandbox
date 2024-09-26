from flask import Flask, jsonify, request
import mysql.connector
import json

app = Flask(__name__)


@app.route('/parking', methods=['POST'])
def insert_data():
    data = request.data
    dataDict = json.loads(data)
    attitude = dataDict["double"]
    longitude = dataDict["double"]
    pageNumber = dataDict["int"]
    pageSize = dataDict["pageSize"]
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = "insert into parking values(NULL,'" + str(attitude) + "," + str(longitude) + "," + str(
        pageNumber) + "," + str(pageSize) + ")"
    cursor.execute(_SQL)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(
        dataDict), 200



if __name__ == "__main__":
    app.run(debug=True)
