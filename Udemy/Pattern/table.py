num = int(input("Enter number to create table: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

print("Printing reverse table...")
for i in range(10, 0, -1):
    print(f"{num} X {i} = {num * i}")