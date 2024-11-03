# Class Constructors

# 2 types
# Default Constructors
# Parameterised Constructors

class Study:
    #default constructor
    def __init__(self):
        self.course = "Python Programming"

    #methods to access data members of default constructor 
    def access(self):
        print(self.course)

obj = Study()
obj.access()
