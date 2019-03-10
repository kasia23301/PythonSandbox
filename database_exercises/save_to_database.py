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
            sql = "Insert into Parking Values(NULL, '{0}', '{1}', {2}, {3}, {4}, {5}, {6})".format(row[0], row[1],
                                                                                                   row[2],
                                                                                                   row[3], row[4],
                                                                                                   row[5], row[6])
            cursor.execute(sql)
        conn.commit()
        cursor.close()
