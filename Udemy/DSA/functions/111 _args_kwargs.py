# Arbitary Arguments
# *args # *kwargs

def intro(**data):
    print("Datatype Args: ", type(data))
    for key, value in data.items():
        print("{} : {}".format(key, value))

intro(firstName = "Aaditya", lastName = "Deshmukh", age = 20, mobile = 789456)