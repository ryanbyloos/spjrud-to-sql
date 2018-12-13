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
from src.Database   import Database, db


def set_db(db_name):
    Database.db = Database(db_name)
    conn = sql.connect(db_name+'.db')
    c = conn.cursor()
    Database.db.c = c
    return c