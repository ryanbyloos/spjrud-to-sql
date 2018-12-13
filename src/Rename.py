from src.Relation import Relation
from src.Attribute import Attribute

class Rename(Relation):
    def __init__(self, attr, new_name, subrelation):
    
        if not isinstance(attr, Attribute):
            raise TypeError('The first argument must be an attribute')
        
        if not isinstance(new_name, str):
            raise TypeError('The new name must be a string')

        self.attr, self.new_name, self.subrelation = attr, new_name, subrelation
        

    def compile(self):
        return "ALTER TABLE ({0}) RENAME COLUMN {1} TO {2}".format(self.subrelation.compile(), self.attr.name, self.new_name)