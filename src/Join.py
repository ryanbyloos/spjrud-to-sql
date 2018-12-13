from src.Relation import Relation
from src.Attribute import Attribute

class Join(Relation):
    def __init__(self, subrelation1, subrelation2):
        
        if not (isinstance(subrelation1, Relation) or isinstance(subrelation2, Relation)):
            raise TypeError('The subrelations must be relations')
            
        self.subrelation1, self.subrelation2 = subrelation1, subrelation2
    
    def compile(self):
        return "SELECT * FROM (({0}) Natural JOIN ({1}))".format(self.subrelation1.compile(), self.subrelation2.compile())