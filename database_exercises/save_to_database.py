import mysql.connector
import csv

if __name__ == "__main__":
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}

    csv_data = csv.reader(file('backup.csv'))
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    for row in csv_data:
        sql = """'INSERT INTO Parking (parkingName, parkingAddress, attitude, longitude, distance, freeSpaces, dataVeracity) VALUES (""" + row + """)'"""
        cursor.execute()
        conn.commit()
        cursor.close()
