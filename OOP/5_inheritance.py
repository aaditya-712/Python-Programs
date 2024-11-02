# Inheritance

# Parent class
class Animal:
    def walk(self):
        print("Walking...")


# child class
class Dog(Animal):
    def bark(self):
        print("Dog is Barking.")


# child class
class Cat(Animal):
    def meow(self):
        print("Cat is Meowing.")


# object instanciation
obj = Dog()
obj.walk()
obj.bark()

obj1 = Cat()
obj1.meow()
obj1.walk()
