import sqlite3 as sql

from src.Select     import Select   as S
from src.Project    import Project  as P
from src.Join       import Join     as J
from src.Rename     import Rename   as R
from src.Union      import Union    as U
from src.Diff       import Diff     as D
from src.Relation   import Relation as Rel
from src.Attribute  import Attribute as Attr
from src.Constant   import Constant as Const
from src.Database   import Database, db


def setup(db_name):
    Database.db = Database(db_name)
    conn = sql.connect(db_name+'.db')
    c = conn.cursor()
    Database.db.c = c
    return c