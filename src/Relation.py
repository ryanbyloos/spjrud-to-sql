class Relation():

    def __init__(self, name=""):

        self.name = name
        self.check_args()

    def check_args(self):

        if not isinstance(self.name, str):
            raise Exception("A relation name must be a string.")

    def compile(self):
        return self.name
