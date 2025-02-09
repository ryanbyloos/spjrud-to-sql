import sqlite3 as sql


class Database:

    def __init__(self, db_name, ext='.db'):
        if db_name != None:
            self.db_name = db_name
            self.conn = sql.connect(db_name+ext)
            self.c = self.conn.cursor()

    def query(self, spjrud_query):
        self.table = spjrud_query.compile()
        self.c.execute(spjrud_query.compile())
        self.output = self.c.fetchall()
        return self.output


current = Database(None)
