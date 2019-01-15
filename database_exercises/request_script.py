import requests
import mysql.connector

if __name__ == "__main__":
    r = requests.get('https://parking-finder-spring.herokuapp.com/api/v1/parking/public/nearToLocation')
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'Parking_finder'}
    conn = mysql.connector.connect(**dbconfig)
    parkingName = r["parkingName"]
    parkingAddress = r["parkingAddress"]
    attitude = r["attitude"]
    longitude = r["longitude"]
    freeSpaces = r["freeSpaces"]
    capacity = r["capacity"]
    rating = r["rating"]
    _SQL = "insert into parking values(NULL,'" + str(parkingName) + "'," + str(parkingAddress) + "," + str(
        attitude) + "," + str(longitude) + "," + str(freeSpaces) + "," + str(capacity) + ","
    str(rating) + ")"
    cursor = conn.cursor()
    cursor.execute(_SQL)
