import sqlite3 as sql


class Database:
    def __init__(self, db_name='example'):
        self.db_name = db_name
        self.conn = sql.connect(db_name+'.db')
        self.c = self.conn.cursor()

    def set_db(self, db_name):
        self.db_name = db_name
        self.conn = sql.connect(db_name+'.db')
        self.c = self.conn.cursor()

db = Database('example')