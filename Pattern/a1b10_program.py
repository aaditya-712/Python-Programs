str1 = input("Enter alphabet 1: ")
num1 = int(input("Enter how many times to print: "))

str2 = input("Enter alphabet 2: ")
num2 = int(input("Enter how many times to print: "))

for i in range(0, num1):
    print(f"{str1}", end="")

for j in range(0, num2):
    print(f"{str2}", end="")