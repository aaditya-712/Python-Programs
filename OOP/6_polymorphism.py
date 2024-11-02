# Polymorphism

class Bulbul:
    def fly(self):
        print("Bulbul can fly.")
    def swim(self):
        print("Bulbul can't swim.")


class Ostrich:
    def fly(self):
        print("Ostrich can't fly.")
    def swim(self):
        print("Ostrich can swim.")


def flying(bird):
    bird.fly()
    bird.swim()

obj1 = Bulbul()
obj2 = Ostrich()

flying(obj1)
flying(obj2)
