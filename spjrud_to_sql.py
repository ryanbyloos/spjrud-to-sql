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