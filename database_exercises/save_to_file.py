import mysql.connector

if __name__ == "__main__":
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}

    _SQL = '''select*from parkingfinder'''

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    f = open("datafile.txt", "a+")
    for i in range(1):
        f.write(_SQL)
    cursor.execute(_SQL)
    conn.commit()
