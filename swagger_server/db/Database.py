import os
import psycopg2

from swagger_server.db.queries import *

DATABASE_URL = os.getenv("DATABASE_URL", "ec2-54-217-224-85.eu-west-1.compute.amazonaws.com")
DATABASE_NAME = os.getenv("DATABASE_NAME", "dbumdeiqr7ebbi")
DATABASE_USER = os.getenv("DATABASE_USER", "cyzchzivqmaqhz")
DATABASE_PASS = os.getenv("DATABASE_PASS", "aa8492d1044229569475e0095b565843485352d1390011985d185e3d106cdd7e")


class PostgresDB:

    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(host=DATABASE_URL, dbname=DATABASE_NAME, user=DATABASE_USER,
                                     password=DATABASE_PASS,
                                     port=5432)

    def __execute(self, query, args=None):
        __cursor = self.conn.cursor()
        __cursor.execute(query, args)
        __output = []

        if __cursor.description is not None:
            for item in __cursor:
                __output.append(item)
        __cursor.close()
        return __output

    def close(self):
        self.conn.commit()
        self.conn.close()

    def get_locations(self):
        self.connect()
        locations = self.__execute(GET_LOCATIONS)
        self.close()
        return locations

    def insert_new_location(self, _location: str):
        self.connect()
        self.__execute(NEW_LOCATION, {"location": _location})
        self.close()

    def get_last_location(self):
        self.connect()
        last_location = self.__execute(GET_LAST_LOCATION)
        self.close()
        return last_location
