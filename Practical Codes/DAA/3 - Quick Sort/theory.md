### 🔹 Quick Sort Function

```python
def quick_sort(arr):
```

Defines a function called `quick_sort` that takes a list `arr` as an input.

---

```python
    """
    Quick Sort Algorithm that returns a new sorted list.
    Uses recursion and selects the last element as pivot.
    """
```

A **docstring** that briefly explains:

- This is the Quick Sort algorithm.
- It returns a **new sorted list** (it does not modify the original list).
- It uses **recursion** and selects the **last element** as the pivot.

---

```python
    if len(arr) <= 1:
        return arr  # Base case: single-element list is already sorted
```

This is the **base case** for recursion.  
If the array has **0 or 1 elements**, it’s already sorted — so return it as-is.

---

```python
    pivot = arr[-1]  # Choosing the last element as pivot
```

The pivot is chosen as the **last element** of the array.  
In Python, `arr[-1]` gives the last item in the list.

---

```python
    left = [x for x in arr[:-1] if x <= pivot]  # Elements ≤ pivot
```

This is a **list comprehension**:

- `arr[:-1]` means: all elements except the pivot (last element).
- This builds a new list `left` of all elements **less than or equal to** the pivot.

---

```python
    right = [x for x in arr[:-1] if x > pivot]  # Elements > pivot
```

Another list comprehension:

- Same as above, but now it collects elements **greater than** the pivot.
- This becomes the `right` list.

---

```python
    return quick_sort(left) + [pivot] + quick_sort(right)
```

Now we **recursively call** quick_sort on both the `left` and `right` halves:

- Sort `left`
- Add the `pivot`
- Sort `right`

Then we **combine** them as:

```
(sorted left) + [pivot] + (sorted right)
```

This is the **heart of Quick Sort** – divide, conquer, and combine.

---

### 🔹 Main Program

```python
print("Enter elements separated by spaces:")
```

Asks the user to input numbers separated by spaces.

---

```python
arr = list(map(int, input().split()))
```

- `input()` reads the input as a string.
- `.split()` breaks the string into a list of words/numbers.
- `map(int, ...)` converts each to an integer.
- `list(...)` collects them into a list called `arr`.

---

```python
print("Original array:", arr)
```

Prints the original, unsorted array for reference.

---

```python
sorted_arr = quick_sort(arr)
```

Calls the `quick_sort()` function and stores the **new sorted list** in `sorted_arr`.

---

```python
print("Sorted array:  ", sorted_arr)
```

Prints the final sorted result.

---

### 🔚 Summary:

- ✅ This is a **recursive** Quick Sort.
- ✅ It creates **new lists** instead of sorting in-place.
- ✅ It shows the power of Python’s **list comprehensions** and **recursion**.

---

### ✅ **Quick Sort Analysis Table**

| **Aspect**        | **Complexity**        | **Reason / Explanation**                                                                                  |
|------------------|------------------------|-------------------------------------------------------------------------------------------------------------|
| **Best Case**     | **O(n log n)**         | Occurs when the pivot divides the array into two **equal halves** at each step. Balanced recursion.         |
| **Average Case**  | **O(n log n)**         | On average, pivot divides the array reasonably well. Recursive tree has height log n, with n comparisons.   |
| **Worst Case**    | **O(n²)**              | Happens when pivot is the **smallest or largest** element each time (highly unbalanced splits).             |
| **Space (In-place)**  | **O(log n)**     | Only log n stack frames needed in ideal cases due to recursive calls. No extra array used for sorting.      |
| **Space (Unbalanced Recursion)** | **O(n)** | Worst case recursion depth (like in sorted/reverse arrays) may cause n recursive calls.                    |

---

### 🔍 Explanation Breakdown:

#### 🔹 Time Complexity
- **Best Case**: If pivot always lands in the center ⇒ balanced recursive calls ⇒ `n log n`.
- **Average Case**: Statistically, pivot divides the array fairly evenly ⇒ `n log n`.
- **Worst Case**: Pivot always lands at one extreme ⇒ one side has n-1 elements ⇒ becomes `n + n-1 + n-2 + ... + 1 = O(n²)`.

#### 🔹 Space Complexity
- **Quick Sort is in-place**: It uses no additional array (unlike Merge Sort).
- Stack usage depends on **depth of recursion**:
  - **Balanced** partition ⇒ **O(log n)**
  - **Unbalanced** (worst case) ⇒ **O(n)**

---