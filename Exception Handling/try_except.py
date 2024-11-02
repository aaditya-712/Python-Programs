# exception handling

try:
    age = int(input("Enter your age: "))
    print(age)

except ValueError:
    print("Enter valid input")