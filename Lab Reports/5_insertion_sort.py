def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j>=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printArray(arr):
    for element  in arr:
        print(element, end=" ")
        print()
arr = [12, 11, 13, 5, 6]
print("Original array:", end=" ")
printArray(arr)

insertionSort(arr)
print("Sorted array:", end=" ")
printArray(arr)