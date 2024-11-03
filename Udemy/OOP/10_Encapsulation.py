# Encapsulation

class Lappy:
    def __init__(self):
        self.__maxPrice = 2500

    def sell(self):
        print("Selling Price: ", self.__maxPrice)

    def setMaxPrice(self, price):
        self.__maxPrice = price


c = Lappy()
c.sell()

#change the price
c.__maxPrice = 4500
c.sell()

#using setter method / function
c.setMaxPrice(5000)
c.sell()