from src.Relation import Relation
from src.Attribute import Attribute

class Select(Relation):
    def __init__(self, attr1, attr2, subrelation):
        
        self.attr1, self.attr2, self.subrelation = attr1, attr2, subrelation

        if not isinstance(self.attr1, Attribute):
            raise TypeError('The first argument must be an attribute.')

        if not isinstance(self.subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')
        
        if isinstance(self.attr2, str): #TODO
        #select "attribute = constant"
            pass

        elif isinstance(self.attr2, Attribute): #TODO
        #select "attribute = attribute"
            pass

        self.condition = "{0}={1}".format(attr1.name, attr2.name)
    
    def compile(self):
        return "SELECT * FROM ({0}) WHERE {1}".format(self.subrelation.compile(), self.condition)