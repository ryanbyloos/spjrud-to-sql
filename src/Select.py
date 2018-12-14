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
        argtype = {}
        Database.db.c.execute("PRAGMA table_info({0})".format(self.subrelation.compile()))
        details = Database.db.c.fetchall()
        for i in details:
            argtype[i[1]] = i[2]

        if not isinstance(self.attr1, Attribute):
            raise TypeError('The first argument must be an attribute.')

        if not (isinstance(self.attr2, Attribute) or isinstance(self.attr2, Constant)):
            raise TypeError('The second argument must be either an argument or a constant.')
        
        if isinstance(self.attr2, Attribute) and not argtype[self.attr1.name] == argtype[self.attr2.name]:
            raise TypeError('The first attribute doesn\'t match the second one.')

        if not isinstance(self.subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')

    def compile(self):
        return "SELECT * FROM {0} WHERE {1}".format(self.subrelation.compile(), self.condition)