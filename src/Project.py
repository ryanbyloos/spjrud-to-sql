from src.Relation import Relation
from src.Attribute import Attribute

class Project(Relation):
    def __init__(self, attr_list, subrelation):

        self.attr = ""

        if not isinstance(attr_list, list):
            raise TypeError('The first argument must be a list of attributes.')

        if not isinstance(subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')

        for e in attr_list:
            self.attr+=e.name
            self.attr+=", "
        self.attr = self.attr[:-2] # There is one useless ", "
        self.subrelation = subrelation
        
    def compile(self):
        return "SELECT {0} FROM ({1})".format(self.attr, self.subrelation.compile())