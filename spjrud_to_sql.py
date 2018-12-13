import sqlite3 as sql

from src.Relation   import Relation
from src.Select     import Select
from src.Project    import Project
from src.Join       import Join
from src.Rename     import Rename
from src.Union      import Union
from src.Diff       import Diff
from src.Attribute  import Attribute
from src.Constant   import Constant
from src.Database   import Database

conn = sql.connect('example.db')
c = conn.cursor()

def set_db(db_name):
    Database.db = Database(db_name)
    c = Database.db.c



# if __name__ == "__main__":
    
#     # c.execute('''CREATE TABLE A (date text, trans text, symbol text, qty real, price real)''')
# # c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# # c.execute("INSERT INTO stocks VALUES ('2018-12-13', 'SELL', 'FUCKYOU', 200, 1.4)")
# # c.execute(''' CREATE TABLE A( Name TEXT, Country TEXT, Population NUMERIC, PRIMARY KEY(Name, Country))''')
# # c.execute("INSERT INTO Cities VALUES ('Bergen', 'Belgium', 20.3)")
# # c.execute("INSERT INTO Cities VALUES ('Bergen', 'Norway', 30.5)")
# # c.execute("INSERT INTO Cities VALUES ('Brussels', 'Belgium', 370.6)")

    
#     # db.c.execute(s.Select(Attribute('Name'), Attribute('Country'), Relation('Cities')).compile())
#     db.c.execute(Select(Attribute('Name'), Attribute('Population'), Relation('Cities')).compile())
#     # db.c.execute("SELECT Name, Country FROM Cities")
#     print(db.c.fetchall())
#     # conn.commit()
#     db.conn.close()