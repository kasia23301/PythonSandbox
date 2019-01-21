import json

import requests
import mysql.connector

if __name__ == "__main__":
    r = requests.get(
        'https://parking-finder-spring.herokuapp.com/api/v1/parking/public/nearToLocation?attitude=51.107077&longitude=17.057669&pageNumber=0&pageSize=20')
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}
    conn = mysql.connector.connect(**dbconfig)
    r = json.loads(r.content)
    cursor = conn.cursor()
    for elem in r:
        parkingName = elem["parkingName"]
        parkingAddress = elem["parkingAddress"]
        attitude = elem["attitude"]
        longitude = elem["longitude"]
        distance = elem["distance"]
        freeSpaces = elem["freeSpaces"]
        dataVeracity = elem["dataVeracity"]
        _SQL = "insert into parking values(NULL,'" + str(parkingName) + "'," + str(parkingAddress) + "," + str(
            attitude) + "," + str(longitude) + "," + str(distance) + "," + str(freeSpaces) + ","
        str(dataVeracity) + ")"
        cursor.execute(_SQL)
    conn.commit()
