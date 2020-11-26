import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASS = os.getenv("DATABASE_PASS")
connection = psycopg2.connect(host=DATABASE_URL, dbname=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASS,
                              port=5432, sslmode="require")
cursor = connection.cursor()
print(connection)

postgreSQL_select_Query = "select * from usuarios"

cursor.execute(postgreSQL_select_Query)

print("Selecting rows from mobile table using cursor.fetchall")
mobile_records = cursor.fetchall()

print(mobile_records)
cursor.close()
connection.close()
