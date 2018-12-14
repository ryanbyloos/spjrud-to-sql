from src.Relation import Relation
from src.Attribute import Attribute

class Diff(Relation):
    def __init__(self, subrelation1, subrelation2):
        self.subrelation1, self.subrelation2 = subrelation1, subrelation2
        self.check_args()
    
    def check_args():
        if not (isinstance(self.subrelation1, Relation) or isinstance(self.subrelation2, Relation)):
            raise TypeError('The subrelations must be relations')
            
    def compile(self):
        return "(SELECT * FROM {0}) EXCEPT (SELECT * FROM {1})".format(self.subrelation1.compile(), self.subrelation2.compile())