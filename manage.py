import psycopg2
from contextlib import closing
from datetime import datetime
from flask import Flask
from flask_script import Manager
from app import create_app
from instance.config_db import connection 

app = create_app('development')
manager = Manager(app)


@manager.command
def init_dev_db():
    with closing(connection()) as conn, conn.cursor() as cur:
        with app.open_instance_resource('createdb.sql', mode='r') as f:
            cur.execute(f.read())
        conn.commit()

@manager.command
def init_test_db():
    with closing(connection()) as conn, conn.cursor() as cur:
        with app.open_instance_resource('createdb.sql',mode='r') as f:
            cur.execute(f.read())
        conn.commit()

@manager.command
def drop_tables():
    with closing(connection()) as conn, conn.cursor() as cur:
        commands = (
            """DROP TABLE IF EXISTS users CASCADE""",
            """DROP TABLE IF EXISTS incidents CASCADE""",
            """DROP TYPE IF EXISTS incident_type CASCADE""",
            """DROP TYPE IF EXISTS current_status CASCADE""")
        for command in commands:
            cur.execute(command)
        conn.commit()


if __name__ == '__main__':
    manager.run()