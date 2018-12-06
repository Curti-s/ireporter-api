import psycopg2
from contextlib import closing
from datetime import datetime
from flask import Flask
from flask_script import Manager
from app import create_app

app = create_app('development')
manager = Manager(app)

def connection():
    """ Read connection params and connect to db"""
    # read connection parameters
    conn = psycopg2.connect(dbname="ireporter_api")
    return conn

@manager.command
def init_db():
    with closing(connection()) as conn, conn.cursor() as cur:
        with app.open_instance_resource('createdb.sql', mode='r') as f:
            cur.execute(f.read())
        conn.commit()

if __name__ == '__main__':
    manager.run()