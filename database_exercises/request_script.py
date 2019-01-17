import requests
import mysql.connector

if __name__ == "__main__":
    r = requests.get('https://parking-finder-spring.herokuapp.com/api/v1/parking/public/nearToLocation')
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}
    conn = mysql.connector.connect(**dbconfig)
    for elem in r:
        parkingName = elem["parkingName"]
        parkingAddress = elem["parkingAddress"]
        attitude = elem["attitude"]
        longitude = elem["longitude"]
        freeSpaces = elem["freeSpaces"]
        capacity = elem["capacity"]
        rating = elem["rating"]
    _SQL = "insert into parking values(NULL,'" + str(parkingName) + "'," + str(parkingAddress) + "," + str(
        attitude) + "," + str(longitude) + "," + str(freeSpaces) + "," + str(capacity) + ","
    str(rating) + ")"
    cursor = conn.cursor()
    cursor.execute(_SQL)
    conn.commit()
