class Bird:
    def intro(self):
        print("Many types of birds here.")

    def flight(self):
        print("Most of the birds will fly and some cannot")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly easily.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


# class instanciating
obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

# class objects calling
obj_bird.intro()
obj_bird.flight()

# child class object calling
obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
