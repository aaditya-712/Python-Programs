# Abstraction
from abc import ABC, abstractmethod

class Car(ABC):
    def milage(self):
        pass

class Tesla(Car):
    def milage(self):
        print("Milage is 30Kmpl.")

class KIA(Car):
    def milage(self):
        print("Milage is 24Kmpl.")



#Object instantiate from Abstract class
t = Tesla()
t.milage()

k = KIA()
k.milage()
