rows = int(input("Enter the number of rows: "))
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    i += 1
    print()