import mysql.connector

if __name__ == "__main__":
    dbconfig = {'host': '127.0.0.1',
                'user': 'root',
                'password': 'arogontaldo',
                'database': 'parkingfinder'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    Delete_all_query = """truncate table Parking"""
    cursor.execute(Delete_all_query)
    conn.commit()
