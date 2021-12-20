import psycopg2
from flask import g

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            user="dbuser",
            password="secreto",
            host="db",
            port="5432",
            database="db"
        )
    return g.db
