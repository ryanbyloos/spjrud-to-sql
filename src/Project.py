from src.Relation import Relation
from src.Attribute import Attribute
from src.Database import Database, current


class Project(Relation):

    def __init__(self, attr_list, subrelation):
        self.subrelation, self.attr_list = subrelation, attr_list
        self.check_args()
        self.attr = ""
        for e in self.attr_list:
            self.attr += e.name
            self.attr += ", "
        self.attr = self.attr[:-2]

    def check_args(self):

        if not isinstance(self.attr_list, list):
            raise Exception('The first argument must be a list of attributes.')

        for e in self.attr_list:
            if not isinstance(e, Attribute):
                raise Exception(
                    'The first argument must be a list of attributes.')

        if not isinstance(self.subrelation, Relation):
            raise Exception('The subrelation must be a relation.')

        argtype = {}
        Database.current.c.execute("DROP TABLE IF EXISTS tmp")
        Database.current.c.execute(
            "CREATE TABLE tmp AS SELECT * FROM ({0})".format(self.subrelation.compile()))
        Database.current.c.execute("PRAGMA table_info(tmp)")
        arglist = Database.current.c.fetchall()

        for i in arglist:
            argtype[i[1]] = i[2]
        for j in self.attr_list:
            if j.name not in argtype:
                raise Exception(j.name+' isn\'t in the relation.')

    def compile(self):
        return "SELECT {0} FROM ({1})".format(self.attr, self.subrelation.compile())
