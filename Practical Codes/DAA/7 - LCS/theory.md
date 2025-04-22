
## 🔍 Function Definition

```python
def lcs(X, Y):
```

Defines a function `lcs` that takes two input strings `X` and `Y`.  
It will compute:

- The **length** of the longest common subsequence
- The **subsequence itself**

---

### 🔹 Step 1: Get Lengths

```python
    m = len(X)
    n = len(Y)
```

- `m` is the length of string `X`
- `n` is the length of string `Y`

We will build a table of size `(m+1) x (n+1)` to store LCS results of substrings.

---

### 🔹 Step 2: Initialize DP Table

```python
    dp = [[0] * (n + 1) for _ in range(m + 1)]
```

- `dp[i][j]` will store the length of the **LCS of X[0…i-1] and Y[0…j-1]**
- Extra row and column (size +1) initialized to `0` so we can handle base cases (empty substrings)

---

### 🔹 Step 3: Fill the Table (Bottom-Up)

```python
    for i in range(1, m + 1):
        for j in range(1, n + 1):
```

We loop through the table **from (1,1) to (m,n)**

---

#### Match Case

```python
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
```

If characters match, we **extend the LCS**:

- Add 1 to the LCS length of the previous diagonal cell: `dp[i-1][j-1]`

Example: if `X[i-1] == Y[j-1] == 'A'`, then add `1`

---

#### Mismatch Case

```python
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

If characters don’t match:

- We take the **maximum** of:
  - Excluding the current character of `X` (`dp[i-1][j]`)
  - Excluding the current character of `Y` (`dp[i][j-1]`)

---

### 🔹 Step 4: Reconstruct LCS String

```python
    lcs_str = []
    i, j = m, n
```

- We start from the **bottom-right** corner of the table
- `lcs_str` will hold characters of the final LCS (in reverse)

---

```python
    while i > 0 and j > 0:
```

Loop until we reach the top or left edge of the table

---

#### Case: Characters Match

```python
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
```

- Add this matching character to the `lcs_str`
- Move diagonally up-left

---

#### Case: Move in Direction of Max

```python
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
```

- If top cell is greater → move **up**
- If left cell is greater → move **left**
- We follow the **path of the greater value**, which represents the longer subsequence so far

---

### 🔹 Step 5: Return Results

```python
    return dp[m][n], ''.join(reversed(lcs_str))
```

- `dp[m][n]` is the **length** of the LCS
- `lcs_str` is reversed because we built it **backwards**
- `''.join(...)` converts the character list to a string

---

## ✅ Main Program

```python
X = input("Enter first string: ")
Y = input("Enter second string: ")
```

Takes input strings from the user.

---

```python
length, sequence = lcs(X, Y)
```

Calls the `lcs()` function with the input strings  
Returns both the **length** and the **sequence**

---

```python
print(f"\nLength of LCS: {length}")
print(f"LCS: {sequence}")
```

Displays the final results.

---

### 🧾 Example Input:

```
Enter first string: AGGTAB
Enter second string: GXTXAYB
```

### ✅ Output:

```
Length of LCS: 4
LCS: GTAB
```

---

### ✅ **LCS (Longest Common Subsequence) Analysis Table**

| **Aspect**         | **Complexity**         | **Reason / Explanation**                                                                 |
|--------------------|------------------------|--------------------------------------------------------------------------------------------|
| **Best Case**       | **O(m × n)**           | All characters match or mismatch must be checked; DP always fills the table regardless.   |
| **Average Case**    | **O(m × n)**           | The algorithm fills an `m × n` table regardless of string similarity.                     |
| **Worst Case**      | **O(m × n)**           | Strings have no common subsequence (all mismatches), so full table must be filled.        |
| **Space Complexity (Full Table)** | **O(m × n)** | Stores a DP table of size `(m+1) × (n+1)` to keep track of subproblem results.             |
| **Space Optimized (1D)**          | **O(min(m, n))** | Only two rows/columns needed at a time; applicable when just LCS length is required.     |

---

### 🔍 Explanation:

#### 🔹 Time Complexity:

- LCS is solved by **building a DP table** of size `(m+1) × (n+1)` where:
  - `m = length of string X`
  - `n = length of string Y`
- Each cell requires constant time to compute → Total time = **O(m × n)** in **all cases**.

There is **no variation** between best, average, and worst cases in terms of time, because the **entire table is always filled**.

---

#### 🔹 Space Complexity:

- **Standard DP**: Stores the full table → **O(m × n)**
- **Optimized**: If we only care about the LCS **length**, we can use **two 1D arrays** → **O(min(m, n))**

But if reconstructing the actual sequence, we need the full table.

---

### ✅ Summary Table

| **Metric**         | **Complexity**     | **Explanation**                                                                   |
|--------------------|--------------------|------------------------------------------------------------------------------------|
| **Time (Best)**     | O(m × n)           | Full table filled regardless of input                                             |
| **Time (Average)**  | O(m × n)           | Always builds table based on both string lengths                                  |
| **Time (Worst)**    | O(m × n)           | All characters mismatch → no shortcuts in table filling                           |
| **Space (Standard)**| O(m × n)           | Full DP table needed for length + reconstruction                                  |
| **Space (Optimized)**| O(min(m, n))      | When only LCS **length** is needed, not the sequence itself                      |

---