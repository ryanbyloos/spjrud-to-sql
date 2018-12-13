from src.Relation import Relation
from src.Attribute import Attribute

class Project(Relation):
    def __init__(self, attr, subrelation):

        self.attr, self.subrelation = attr, subrelation

        if not isinstance(attr, Attribute):
            raise TypeError('The first argument must be an attribute.')

        if not isinstance(subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')
        
    def compile(self):
        return "SELECT {0} FROM ({1})".format(self.attr.name, self.subrelation.compile())