# instance/db_config.py

import psycopg2
from instance.config import dbconfig

def connection():
    """ Read connection params and connect to db"""
    # read connection parameters
    params = dbconfig()
    try:
        conn = psycopg2.connect(**params)
        return conn
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_tables():
    pass

def tables():
    pass

