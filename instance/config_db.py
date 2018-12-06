import psycopg2
import os
from flask import current_app


def connection():
    if current_app.config['ENV'] == 'development':
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    elif current_app.config['ENV'] == 'testing':
        conn = psycopg2.connect(os.getenv('DATABASE_URL_TEST'))
    return conn
