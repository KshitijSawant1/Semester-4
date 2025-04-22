def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main Program
print("Enter elements separated by spaces:")
arr = list(map(int, input().split()))

print("Enter the element to search:")
target = int(input())

# Step 1: Sort the array using Bubble Sort
bubble_sort(arr)
print("Sorted array:", arr)

# Step 2: Search using Binary Search
index = binary_search(arr, target)

# Step 3: Display Result
if index != -1:
    print(f"Element found at index {index} in the sorted array")
else:
    print("Element not found in the list")
