import mysql.connector

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
    with open('datafile.txt', 'a') as file:
        for row in result_set:
            file.write("%s, %s, %s, %s, %s, %s, %s" % (
                row["parkingName"], row["parkingAddress"], row["attitude"], row["longitude"], row["distance"],
                row["freeSpaces"], row["dataVeracity"]))

