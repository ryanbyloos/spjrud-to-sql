from src.Relation import Relation
from src.Attribute import Attribute
from src.Database import Database, db

class Rename(Relation):
    def __init__(self, attr, new_name, subrelation):

        self.attr, self.new_name, self.subrelation = attr, new_name, subrelation
        self.check_args()
        self.column_list = self.get_column_list()
        
    def compile(self):
        return "SELECT DISTINCT {0} AS {1} FROM ({2})".format(self.column_list, self.new_name, self.subrelation.compile())
    def check_args(self):

        if not isinstance(self.attr, Attribute):
            raise TypeError('The first argument must be an attribute')
        
        if not isinstance(self.new_name, str):
            raise TypeError('The new name must be a string')

    def get_column_list(self):
        Database.db.c.execute("DROP TABLE IF EXISTS tmp")
        Database.db.c.execute("CREATE TABLE tmp AS SELECT * FROM ({0})".format(self.subrelation.compile()))
        Database.db.c.execute("PRAGMA table_info(tmp)")
        col_list = Database.db.c.fetchall()
        res = ''
        for c in col_list:
            res += c[1]
            res += ", "
        return res[:-2]

