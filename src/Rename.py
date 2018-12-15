from src.Relation import Relation
from src.Attribute import Attribute
from src.Database import Database, current


class Rename(Relation):

    def __init__(self, attr, new_name, subrelation):

        self.attr, self.new_name, self.subrelation = attr, new_name, subrelation
        self.check_args()

    def compile(self):
        return "SELECT DISTINCT {0} AS {1} FROM ({2})".format(self.column_list, self.new_name, self.subrelation.compile())

    def check_args(self):

        if not isinstance(self.attr, Attribute):
            raise TypeError('The first argument must be an attribute.')

        if not isinstance(self.new_name, str):
            raise TypeError('The new name must be a string.')

        if not isinstance(self.subrelation, Relation):
            raise TypeError('The subrelation must be a Relation.')

        self.column_list = self.get_column_list()

        for c in self.col_list:
            if self.new_name == c[1]:
                raise Exception(
                    'The new name is already taken in the relation.')

    def get_column_list(self):
        Database.current.c.execute("DROP TABLE IF EXISTS tmp")
        Database.current.c.execute(
            "CREATE TABLE tmp AS SELECT * FROM ({0})".format(self.subrelation.compile()))
        Database.current.c.execute("PRAGMA table_info(tmp)")
        self.col_list = Database.current.c.fetchall()
        res = ''
        for c in self.col_list:
            res += c[1]
            res += ", "
        return res[:-2]
