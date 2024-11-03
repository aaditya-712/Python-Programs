arr = [25, 11, 7, 75, 56]
max = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]

print("Largest element in the array is:",max)