def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
         return i 
    return -1 
input_list = input("Enter a list of number separated by space :").split()
key = int(input("Enter the key to search:"))
int_list = [int(x)for x in input_list]
result = linear_search(int_list, key)
if result == -1:
    print("Enter not found")
else:
    print(f"Enter found at index:{result}")