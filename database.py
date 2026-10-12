import mysql.connector
def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='Sukanya@409',
        database='car_rental',

        )
    return conn
