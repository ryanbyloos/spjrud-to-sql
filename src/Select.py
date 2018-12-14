from src.Relation import Relation
from src.Attribute import Attribute
from src.Constant import Constant
from src.Database import Database, db


class Select(Relation):

    def __init__(self, attr1, attr2, subrelation):
        self.attr1, self.attr2, self.subrelation = attr1, attr2, subrelation
        self.condition = "{0}={1}".format(attr1.name, attr2.name)
        self.check_args()

    def check_args(self):
        if not isinstance(self.subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')
        Database.db.c.execute("DROP TABLE IF EXISTS tmp")
        Database.db.c.execute(
            "CREATE TABLE tmp AS SELECT * FROM ({0})".format(self.subrelation.compile()))
        Database.db.c.execute("PRAGMA table_info(tmp)")
        arglist = Database.db.c.fetchall()
        argtype = {}
        for i in arglist:
            argtype[i[1]] = i[2]
        if not isinstance(self.attr1, Attribute):
            raise TypeError('The first argument must be an attribute.')
        if not (isinstance(self.attr2, Attribute) or isinstance(self.attr2, Constant)):
            raise TypeError(
                'The second argument must be either an argument or a constant.')
        if isinstance(self.attr2, Attribute) and not argtype[self.attr1.name] == argtype[self.attr2.name]:
            raise TypeError(
                'The first attribute doesn\'t match the second one.')
        try:
            argtype[self.attr1.name]
        except KeyError:
            print(self.attr1.name+' isn\'t in the relation.')
        if isinstance(self.attr2, Attribute):
            try:
                argtype[self.attr2.name]
            except KeyError:
                raise Exception(self.attr2.name+' isn\'t in the relation.')

    def compile(self):
        return "SELECT * FROM {0} WHERE {1}".format(self.subrelation.compile(), self.condition)
