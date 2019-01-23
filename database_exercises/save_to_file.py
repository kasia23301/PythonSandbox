import mysql.connector

if __name__ == "__main__":
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT parkingName, parkingAddress, attitude, longitude, distance, freeSpaces, dataVeracity FROM Parking ")
    result_set = cursor.fetchall()
    for row in result_set:
        print("%s, %s" % (row["parkingName"], row["parkingAddress"], row["attitude"], row["longitude"], row["distance"],
                          row["freeSpaces"], row["dataVeracity"]))
    conn.commit()
