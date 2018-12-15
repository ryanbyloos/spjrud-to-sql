import sqlite3 as sql

from src.Select import Select
from src.Project import Project
from src.Join import Join
from src.Rename import Rename
from src.Union import Union
from src.Diff import Diff
from src.Relation import Relation as Rel
from src.Attribute import Attribute as Attr
from src.Constant import Constant as Cst
from src.Database import Database, current


def set_db(db_name, ext='.db'):
    Database.current = Database(db_name, ext)
    conn = sql.connect(db_name+ext)
    c = conn.cursor()
    Database.current.c = c
    return c


def create_table(table_name, spjrud_query):
    Database.current.c.execute(
        ''' CREATE TABLE {0} AS SELECT * FROM ({1}) '''.format(table_name, spjrud_query))
    print("Table {0} successfully created.".format(table_name))


def s(attr1, attr2, subrelation):
    Database.current.query(Select(attr1, attr2, subrelation))
    return Select(attr1, attr2, subrelation).compile()


def p(attr_list, subrelation):
    Database.current.query(Project(attr_list, subrelation))
    return Project(attr_list, subrelation).compile()


def j(subrelation1, subrelation2):
    Database.current.query(Join(subrelation1, subrelation2))
    return Join(subrelation1, subrelation2).compile()


def r(attr, new_name, subrelation):
    Database.current.query(Rename(attr, new_name, subrelation))
    return Rename(attr, new_name, subrelation).compile()


def u(subrelation1, subrelation2):
    Database.current.query(Union(subrelation1, subrelation2))
    return Union(subrelation1, subrelation2).compile()


def d(subrelation1, subrelation2):
    Database.current.query(Diff(subrelation1, subrelation2))
    return Diff(subrelation1, subrelation2).compile()
