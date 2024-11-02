class Greet:
    # class attribute
    course = "Python for beginner"
    def user_greet(self):
        print("Welcome sir")

    def hello(self):
        print("Hello bro")


wish = Greet()
wish.user_greet()
wish.hello()
print(wish.course)
