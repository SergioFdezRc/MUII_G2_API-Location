import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL", "ec2-54-217-224-85.eu-west-1.compute.amazonaws.com")
DATABASE_NAME = os.getenv("DATABASE_NAME", "dbumdeiqr7ebbi")
DATABASE_USER = os.getenv("DATABASE_USER", "cyzchzivqmaqhz")
DATABASE_PASS = os.getenv("DATABASE_PASS", "aa8492d1044229569475e0095b565843485352d1390011985d185e3d106cdd7e")
connection = psycopg2.connect(host=DATABASE_URL, dbname=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASS,
                              port=5432)
cursor = connection.cursor()
print(connection)

query = "select * from usuarios"

cursor.execute(query)

print("Selecting rows from usuarios table using cursor.fetchall")
users = cursor.fetchall()

print(users)

# close the cursor and the connection pool
cursor.close()
connection.close()
