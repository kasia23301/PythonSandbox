import mysql.connector
import csv

if __name__ == "__main__":
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT parkingName, parkingAddress, attitude, longitude, distance, freeSpaces, dataVeracity FROM Parking ")
    result_set = cursor.fetchall()
    with open("backup.csv", mode="w") as backup:
        backup_writer = csv.writer(backup, delimiter=',')
        for row in result_set:
            backup_writer.writerow("%s, %s, %s, %s, %s, %s, %s\n" % (
                row["parkingName"], row["parkingAddress"], row["attitude"], row["longitude"], row["distance"],
                row["freeSpaces"], row["dataVeracity"]))
