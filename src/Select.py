from src.Relation import Relation
from src.Attribute import Attribute
from src.Constant import Constant
from src.Database import db

class Select(Relation):
    def __init__(self, attr1, attr2, subrelation):
        
        self.attr1, self.attr2, self.subrelation = attr1, attr2, subrelation

        if not isinstance(self.attr1, Attribute):
            raise TypeError('The first argument must be an attribute.')

        if not isinstance(self.subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')
        
        if not self.check_compatibility():
            raise TypeError('The first attribute doesn\'t match the second one.')

        if isinstance(self.attr2, Constant): #TODO
        #select "attribute = constant"
            pass

        elif isinstance(self.attr2, Attribute): #TODO
        #select "attribute = attribute"
            pass

        self.condition = "{0}={1}".format(attr1.name, attr2.name)

    def check_compatibility(self):
        db.c.execute("SELECT typeof({0}) FROM {1}".format(self.attr1.name, self.subrelation.name))
        type1 = db.c.fetchone()[0]
        db.c.execute("SELECT typeof({0}) FROM {1}".format(self.attr2.name, self.subrelation.name))
        type2 = db.c.fetchone()[0]

        return type1 == type2
    
    def compile(self):
        return "SELECT * FROM {0} WHERE {1}".format(self.subrelation.compile(), self.condition)