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

def tables():
    comands = (
        """
        CREATE TABLE IF NOT EXISTS user (
            user_id SERIAL PRIMARY KEY NOT NULL,
            firstname VARCHAR(60) NOT NULL,
            lastname VARCHAR(60) NOT NULL,
            username VARCHAR(60) NOT NULL,
            email VARCHAR(60) NOT NULL,
            phone_number VARCHAR(60),
            registered TIMESTAMP DEFAULT now() NOT NULL,
            isAdmin BOOL NOT NULL 
        )
        """,
        """
            CREATE TYPE type AS ENUM ('redflag','incident')
        """,
        """
            CREATE TYPE current_status AS ENUM('draft', 'under investigation','resolved', 'rejected')
        """,
        """
            CREATE TABLE IF NOT EXISTS incident (
                incident_id SERIAL PRIMARY KEY NO NULL,
                created_on TIMESTAMP DEFAULT now() NOT NULL,
                created_by INT NOT NULL,
                type type,
                location VARCHAR(50),
                status current_status,
                image BYTEA,
                video BYTEA,
                comment VARCHAR(255),
                FOREIGN KEY (created_by)
                    REFERENCES user(user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """)
    return commands


def create_tables():
    try:
        conn = connection()
        cur = conn.cursor()
        statements = tables()

        # create tables
        for statement in statements:
            cur.execute(statement)
        # commit
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

