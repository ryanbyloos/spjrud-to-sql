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
from src.Database import Database, db


def setup(db_name):
    Database.db = Database(db_name)
    conn = sql.connect(db_name+'.db')
    c = conn.cursor()
    Database.db.c = c
    return c


def query(spjrud_query):
    Database.db.c.execute(spjrud_query.compile())
    print(Database.db.c.fetchall())


def s(attr1, attr2, subrelation):
    return query(Select(attr1, attr2, subrelation))


def p(attr_list, subrelation):
    return query(Project(attr_list, subrelation))


def j(subrelation1, subrelation2):
    return query(Join(subrelation1, subrelation2))


def r(attr, new_name, subrelation):
    return query(Rename(attr, new_name, subrelation))


def u(subrelation1, subrelation2):
    return query(Union(subrelation1, subrelation2))


def d(subrelation1, subrelation2):
    return query(Diff(subrelation1, subrelation2))
