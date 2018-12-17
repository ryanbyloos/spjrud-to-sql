from src.Relation import Relation
from src.Attribute import Attribute
from src.Database import Database, current


class Union(Relation):

    def __init__(self, subrelation1, subrelation2):
        self.subrelation1, self.subrelation2 = subrelation1, subrelation2
        self.check_args()

    def check_args(self):
        if not (isinstance(self.subrelation1, Relation) or isinstance(self.subrelation2, Relation)):
            raise Exception('The subrelations must be relations')
        argtype = {}
        Database.current.c.execute("DROP TABLE IF EXISTS tmp1")
        Database.current.c.execute("DROP TABLE IF EXISTS tmp2")
        Database.current.c.execute(
            "CREATE TABLE tmp1 AS SELECT * FROM ({0})".format(self.subrelation1.compile()))
        Database.current.c.execute("PRAGMA table_info(tmp1)")
        r1 = Database.current.c.fetchall()
        len_r1 = len(r1)
        Database.current.c.execute(
            "CREATE TABLE tmp2 AS SELECT * FROM ({0})".format(self.subrelation2.compile()))
        Database.current.c.execute("PRAGMA table_info(tmp2)")
        r2 = Database.current.c.fetchall()
        len_r2 = len(r2)
        if len_r1 != len_r2:
            raise Exception(
                'The two subrelations must have the same amount of columns.')
        for i in range(len_r2):
            if r1[i][2] != r2[i][2] or r1[i][1] != r2[i][1]:
                raise Exception(
                    'The elements of the two subrelations must be the same.')

    def compile(self):
        return "SELECT * FROM ({0}) UNION SELECT * FROM ({1})".format(self.subrelation1.compile(), self.subrelation2.compile())
