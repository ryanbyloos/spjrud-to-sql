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

if __name__ == "__main__":
    
    conn = sql.connect('example.db')
    c = conn.cursor()
    # c.execute('''CREATE TABLE stocks
    #             (date text, trans text, symbol text, qty real, price real)''')
    # c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    # c.execute("INSERT INTO stocks VALUES ('2018-12-13', 'SELL', 'FUCKYOU', 200, 1.4)")
    # c.execute(''' CREATE TABLE Cities(
    #                 Name TEXT, Country TEXT, Population NUMERIC,
    #                 PRIMARY KEY(Name, Country))''')
    # c.execute("INSERT INTO Cities VALUES ('Bergen', 'Belgium', 20.3)")
    # c.execute("INSERT INTO Cities VALUES ('Bergen', 'Norway', 30.5)")
    # c.execute("INSERT INTO Cities VALUES ('Brussels', 'Belgium', 370.6)")
    
    def check_compatibility(attr1, attr2, table):
        c.execute("SELECT typeof({0}) FROM {1}".format(attr1, table))
        type1 = c.fetchone()[0]
        c.execute("SELECT typeof({0}) FROM {1}".format(attr2, table))
        type2 = c.fetchone()[0]
        return type1 == type2

    print(check_compatibility('Name', 'Country', 'Cities'))
    # conn.commit()
    conn.close()