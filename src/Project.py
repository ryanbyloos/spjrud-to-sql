from src.Relation import Relation
from src.Attribute import Attribute
from src.Database import db

class Project(Relation):
    def __init__(self, attr_list, subrelation):

        self.attr = ""

        if not isinstance(attr_list, list):
            raise TypeError('The first argument must be a list of attributes.')

        if not isinstance(subrelation, Relation):
            raise TypeError('The subrelation must be a relation.')

        if not self.check_args():
            raise TypeError('One attribute isn\'t in the relation.')

        for e in attr_list:
            self.attr+=e.name
            self.attr+=", "
        self.attr = self.attr[:-2] # There is one useless ", "
        self.subrelation, self.attr_list = subrelation, attr_list

    def check_args(self):
        argtype = {}
        details = db.c.execute("PRAGMA table_info({0})".format(self.subrelation.compile()))
        for i in details:
            argtype[i[1]] = i[2]
        for j in self.attr_list:
            if argtype[j] == None:
                return False
        return True
        
    def compile(self):
        return "SELECT {0} FROM ({1})".format(self.attr, self.subrelation.compile())