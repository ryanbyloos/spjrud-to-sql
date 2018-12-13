from src.Relation import Relation
from src.Attribute import Attribute

class Rename(Relation):
    def __init__(self, attr, new_name, subrelation):
        
        self.attr, self.new_name, self.subrelation = attr, new_name, subrelation

        if not isinstance(self.attr, Attribute):
            raise TypeError('The first argument must be an attribute')
        
        if not isinstance(self.new_name, str):
            raise TypeError('The new name must be a string')
        

    def compile(self):
        return "ALTER TABLE ({0})\
                RENAME COLUMN {1} TO {2}".format(self.subrelation, self.attr.name, self.new_name)