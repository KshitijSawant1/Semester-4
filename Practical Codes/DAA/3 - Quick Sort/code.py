def quick_sort(arr):
    """
    Quick Sort Algorithm that returns a new sorted list.
    Uses recursion and selects the last element as pivot.
    """
    if len(arr) <= 1:
        return arr  # Base case: single-element list is already sorted

    pivot = arr[-1]  # Choosing the last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements ≤ pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements > pivot

    return quick_sort(left) + [pivot] + quick_sort(right)


# Main Program
print("Enter elements separated by spaces:")
arr = list(map(int, input().split()))

print("Original array:", arr)

# Step 1: Sort using Quick Sort
sorted_arr = quick_sort(arr)

# Step 2: Output
print("Sorted array:  ", sorted_arr)
