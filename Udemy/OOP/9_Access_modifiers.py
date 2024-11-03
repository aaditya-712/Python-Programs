# Access Modifiers
# public, protected and private

class Greet:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # class constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    #public member function
    def accessPublicMember(self):
        print("Public Data Members: ", self.var1)

    #protected member function
    def accessProtectedMember(self):
        print("Protected Data Members: ", self._var2)

    #private member function
    def accessPrivateMember(self):
        print("Private Data Member: ", self.__var3)

#child class or derived class
class Sub(Greet):
    #default constructor
    def __init__(self, var1, var2, var3):
        Greet.__init__(self, var1, var2, var3)

    def ProtectedMember(self):
        self.accessProtectedMember()


obj = Sub("One", 2, "Three")
obj.accessPublicMember()
obj.ProtectedMember()
obj.accessPrivateMember()
