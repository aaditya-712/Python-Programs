class Car:
    tyre = "CEAT"

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car Stopped..")


class toyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(toyotaCar):
    def __int__(self, type):
        self.type = type

    def color(self, color):
        self.color = color
        print("Your Fortuner with " + self.color + " color is ready.")
        car1.start()
        print("Car is running.")



car1 = Fortuner("Legender")
car1.color("Black")
print(car1.tyre)

