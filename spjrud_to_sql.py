import sqlite3 as sql

from src.Select import Select as S
from src.Project import Project as P
from src.Join import Join as J
from src.Rename import Rename as R
from src.Union import Union as U
from src.Diff import Diff as D
from src.Relation import Relation as Rel
from src.Attribute import Attribute as Attr
from src.Constant import Constant as Cst
from src.Database import Database, current


def set_db(db_name, ext='.db'):
    Database.current = Database(db_name, ext)
    Database.current.conn = sql.connect(db_name+ext)
    Database.current.c = conn.cursor()


def commit():
    Database.current.conn.commit()


def create_table(table_name, spjrud_query):
    Database.current.query(spjrud_query)
    Database.current.c.execute(
        ''' CREATE TABLE {0} AS SELECT * FROM ({1}) '''.format(table_name, Database.current.table))
    print("Table {0} successfully created.".format(table_name))
    print(Database.current.output)


def execute(query):
    if isinstance(query, Rel):
        return Database.current.query(query)
    elif isinstance(query, str):
        return Database.current.c.execute(query)
