
---

### 🔹 **Bubble Sort Function:**
```python
def bubble_sort(arr):
```
Defines a function named `bubble_sort` which takes a list `arr` as input.

```python
    n = len(arr)
```
Stores the length of the list in `n`, so we know how many elements we need to compare.

```python
    for i in range(n - 1):
```
This loop runs `n - 1` times (outer loop). It controls the number of passes. In each pass, the largest unsorted element "bubbles" to the end.

```python
        for j in range(n - i - 1):
```
This inner loop compares adjacent elements. After every pass, the last `i` elements are already sorted, so we reduce comparisons accordingly.

```python
            if arr[j] > arr[j + 1]:
```
Checks if the current element is greater than the next element. If so, they are **out of order**, and we need to swap them.

```python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```
Swaps the two elements using Python’s tuple unpacking (no temp variable needed). This ensures that the smaller number comes first.

---

### 🔹 **Binary Search Function:**
```python
def binary_search(arr, target):
```
Defines a function `binary_search` that takes a **sorted** list `arr` and the `target` value to search for.

```python
    low = 0
    high = len(arr) - 1
```
Initializes the search bounds: `low` is the starting index, `high` is the ending index.

```python
    while low <= high:
```
A loop that keeps running as long as there’s a valid search range.

```python
        mid = (low + high) // 2
```
Finds the middle index of the current search range.

```python
        if arr[mid] == target:
```
If the middle element matches the target, we return its index — **target found**.

```python
            return mid
```
Returns the index where the target was found.

```python
        elif arr[mid] < target:
```
If the middle element is smaller than the target, we search in the **right half**.

```python
            low = mid + 1
```
Adjusts the lower bound to narrow the search to the right half.

```python
        else:
```
If the middle element is greater than the target, we search in the **left half**.

```python
            high = mid - 1
```
Adjusts the upper bound to narrow the search to the left half.

```python
    return -1
```
If the loop finishes without finding the target, return `-1` to indicate "not found."

---

### 🔹 **Main Program Execution:**
```python
print("Enter elements separated by spaces:")
arr = list(map(int, input().split()))
```
- Prompts the user to input numbers (unsorted).
- `input()` takes input as a string.
- `split()` breaks the string into a list of string numbers.
- `map(int, ...)` converts each string to an integer.
- `list(...)` collects all into a Python list named `arr`.

```python
print("Enter the element to search:")
target = int(input())
```
Asks the user to input the element to search for, and converts it to an integer.

---

### 🔹 **Sorting and Searching:**
```python
bubble_sort(arr)
```
Calls the `bubble_sort()` function to sort the array.

```python
print("Sorted array:", arr)
```
Prints the sorted array (important for confirming before binary search).

```python
index = binary_search(arr, target)
```
Calls `binary_search()` with the sorted array and the target value. Stores the result (index or -1) in the variable `index`.

---

### 🔹 **Result Output:**
```python
if index != -1:
    print(f"Element found at index {index} in the sorted array")
```
If index is not -1, print the index where the target was found.

```python
else:
    print("Element not found in the list")
```
Otherwise, inform the user that the element doesn't exist in the array.

---

### ✅ Summary:
- First, the user inputs **unsorted data**.
- The list is sorted using **Bubble Sort**.
- A **Binary Search** is then performed on the sorted list.
- Final output shows whether the target was found and where.
