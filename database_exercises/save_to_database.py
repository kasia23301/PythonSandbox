import mysql.connector
import csv

if __name__ == "__main__":
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}
    with open('backup.csv') as File:
        csv_data = csv.reader(File)
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        for row in csv_data:
            sql = "Insert into Parking Values(%s, %s, %s, %s, %s, %s, %s, %s" (
            row["parkingName"], row["parkingAddress"], row["attitude"], row["longitude"], row["distance"],
            row["freeSpaces"], row["dataVeracity"])
        cursor.execute()
        conn.commit()
        cursor.close()

