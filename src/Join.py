from src.Relation import Relation
from src.Attribute import Attribute
from src.Database import Database, db


class Join(Relation):

    def __init__(self, subrelation1, subrelation2):
        self.subrelation1, self.subrelation2 = subrelation1, subrelation2
        self.check_args()

    def check_args(self):
        if not (isinstance(self.subrelation1, Relation) or isinstance(self.subrelation2, Relation)):
            raise TypeError('The subrelations must be relations')

        argtype = {}
        Database.db.c.execute("DROP TABLE IF EXISTS tmp1")
        Database.db.c.execute("DROP TABLE IF EXISTS tmp2")
        Database.db.c.execute(
            "CREATE TABLE tmp1 AS SELECT * FROM ({0})".format(self.subrelation1.compile()))
        Database.db.c.execute("PRAGMA table_info(tmp1)")
        r1 = Database.db.c.fetchall()
        Database.db.c.execute(
            "CREATE TABLE tmp2 AS SELECT * FROM ({0})".format(self.subrelation2.compile()))
        Database.db.c.execute("PRAGMA table_info(tmp2)")
        r2 = Database.db.c.fetchall()

        for i in r1:
            for j in r2:
                if i[1] == j[1] and i[2] != j[2]:
                    raise TypeError(
                        'Two columns with the same name doesn\'t have the same type')

    def compile(self):
        return "SELECT * FROM (({0}) Natural JOIN ({1}))".format(self.subrelation1.compile(), self.subrelation2.compile())
