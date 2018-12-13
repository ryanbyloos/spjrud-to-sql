from src.Relation import Relation
from src.Attribute import Attribute
from src.Constant import Constant
from src.Database import db

class Select(Relation):
    def __init__(self, attr1, attr2, subrelation):
        
        if not isinstance(attr1, Attribute):
            raise TypeError('The first argument must be an attribute.')

        if not (isinstance(attr2, Attribute) or isinstance(attr2, Constant)):
            raise TypeError('The second argument must be either an argument or a constant.')

        if not isinstance(subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')
        
        if not self.check_compatibility():
            raise TypeError('The first attribute doesn\'t match the second one.')

        self.condition = "{0}={1}".format(attr1.name, attr2.name)
        self.attr1, self.attr2, self.subrelation = attr1, attr2, subrelation

    def check_compatibility(self):
        db.c.execute("SELECT typeof({0}) FROM {1}".format(self.attr1.name, self.subrelation.name))
        type1 = db.c.fetchone()[0]
        db.c.execute("SELECT typeof({0}) FROM {1}".format(self.attr2.name, self.subrelation.name))
        type2 = db.c.fetchone()[0]
        return type1 == type2
    
    def compile(self):
        return "SELECT * FROM {0} WHERE {1}".format(self.subrelation.compile(), self.condition)