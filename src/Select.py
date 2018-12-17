from src.Relation import Relation
from src.Attribute import Attribute
from src.Constant import Constant
from src.Database import Database, current


class Select(Relation):

    def __init__(self, attr1, attr2, subrelation):
        self.attr1, self.attr2, self.subrelation = attr1, attr2, subrelation
        self.condition = "{0}={1}".format(attr1.name, attr2.name)
        self.check_args()

    def check_args(self):
        if not isinstance(self.subrelation, Relation):
            raise Exception('The subrelation must be a relation.')
        Database.current.c.execute("DROP TABLE IF EXISTS tmp")
        Database.current.c.execute(
            "CREATE TABLE tmp AS SELECT * FROM ({0})".format(self.subrelation.compile()))
        Database.current.c.execute("PRAGMA table_info(tmp)")
        arglist = Database.current.c.fetchall()
        argtype = {}
        for i in arglist:
            argtype[i[1]] = i[2]
        if not isinstance(self.attr1, Attribute):
            raise Exception('The first argument must be an attribute.')
        if not (isinstance(self.attr2, Attribute) or isinstance(self.attr2, Constant)):
            raise Exception(
                'The second argument must be either an argument or a constant.')
        if isinstance(self.attr2, Attribute) and not argtype[self.attr1.name] == argtype[self.attr2.name]:
            raise Exception(
                'The first attribute doesn\'t match the second one.')
        if self.attr1.name not in argtype:
            raise Exception(self.attr1.name+' isn\'t in the relation.')
        if isinstance(self.attr2, Attribute):
            if self.attr2.name not in argtype:
                raise Exception(self.attr2.name+' isn\'t in the relation.')

    def compile(self):
        return "SELECT * FROM {0} WHERE {1}".format(self.subrelation.compile(), self.condition)
