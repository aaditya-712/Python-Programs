def product(* args):
    if len(args) == 2:
        p = args[0] * args[1]
        print(p)
    elif len(args) == 3:
        p = args[0] * args[1] * args[2]
        print(p)
    else:
        print("Invalid number of arguments")

product(4, 5)
product(4, 5, 5)

def overloaded_function(*args):
    if len(args) == 1:
        print(f"This is a function with 1 arguments: {args[0]}")
    elif len(args) == 2:
        print(f"This is a function with 2 arguments: {args[0]}, {args[1]}")
    elif len(args) == 3:
        print(f"This is a function with 3 argumrnts: {args[0]}, {args[1]}, {args[2]}")
    else:
        print("Invalid number of arguments")

overloaded_function(10)
overloaded_function(20, 30)
overloaded_function(40, 50, 60)
overloaded_function(70, 80, 90, 100)


