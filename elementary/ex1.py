if __name__ == "__main__":
    print("Hello world")
    zbior = set()
    print(zbior)
    zbior.add('a')
    print(zbior)
    zbior.add('b')
    print(zbior)
    zbior.add('a')
    print(len(zbior))
    print(zbior)

    import mysql.connector

def log_reuest(req,res):

    dbconfig= {'host':'127.0.0.1',
               'user': 'varchar',
               'password': 'varchar',
               'database': 'parkingDB'}

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    _SQL = """insert into parking(name, attitude, longitude, free_spaces, capacity, rating)
            values('Karuzela', 18.432, 23.432, 15, 120, 4)"""

    conn.commit()
    _SQL = """select*from parking"""
    cursor.execute(_SQL)
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()