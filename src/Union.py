from src.Relation import Relation
from src.Attribute import Attribute
from src.Database import Database, db

class Union(Relation):
    def __init__(self, subrelation1, subrelation2):
        
        self.subrelation1, self.subrelation2 = subrelation1, subrelation2
        self.check_args()

    def check_args(self):
        if not (isinstance(self.subrelation1, Relation) or isinstance(self.subrelation2, Relation)):
            raise TypeError('The subrelations must be relations')
        
        argtype = {}
        Database.db.c.execute("PRAGMA table_info({0})".format(self.subrelation1.compile()))
        len_r1 = len(Database.db.c.fetchall())
        Database.db.c.execute("PRAGMA table_info({0})".format(self.subrelation2.compile()))
        len_r2 = len(Database.db.c.fetchall())

        if len_r1 != len_r2:
            raise ValueError('The two subrelations must have the same amount of columns.')


    def compile(self):
        return "SELECT * FROM {0} UNION SELECT * FROM {1}".format(self.subrelation1.compile(), self.subrelation2.compile())