Here is a **complete implementation and analysis** of the **Longest Common Subsequence (LCS)** problem using **Dynamic Programming** in **Python**.

---

## ✅ **1. Problem Statement**
Given two sequences, find the length of their **Longest Common Subsequence (LCS)**.

**Example:**
```plaintext
Input: X = "AGGTAB", Y = "GXTXAYB"
Output: 4
Explanation: LCS is "GTAB"
```

---

## ✅ **2. Python Code (LCS using DP)**

```python
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # To print the LCS string
    lcs_string = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string = X[i - 1] + lcs_string
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], lcs_string


# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
length, subsequence = lcs(X, Y)

print(f"Length of LCS: {length}")
print(f"LCS: {subsequence}")
```

---

## ✅ **3. Working**

- Create a 2D array `dp[m+1][n+1]` where `dp[i][j]` contains length of LCS of `X[0...i-1]` and `Y[0...j-1]`.
- Fill the table by checking:
  - If characters match → `1 + dp[i-1][j-1]`
  - Else → `max(dp[i-1][j], dp[i][j-1])`
- Trace back from `dp[m][n]` to reconstruct the LCS string.

---

## ✅ **4. Recurrence Relation**

\[
T(m, n) =
\begin{cases}
0 & \text{if } i = 0 \text{ or } j = 0 \\
1 + T(m-1, n-1) & \text{if } X[i] = Y[j] \\
\max(T(m-1, n), T(m, n-1)) & \text{otherwise}
\end{cases}
\]

---

## ✅ **5. Time & Space Complexity**

| Case         | Time Complexity | Space Complexity |
|--------------|------------------|------------------|
| Worst / Avg  | O(m × n)         | O(m × n)         |
| Best Case    | O(m × n)         | O(m × n)         |

- `m` and `n` are the lengths of the input strings.
- Can be optimized to `O(n)` space using 2 rows.

---

## ✅ **6. Applications of LCS**

- Bioinformatics (DNA sequence comparison)
- File comparison tools (diff utilities)
- Plagiarism detection
- Data deduplication and compression

---

## ✅ **7. Conclusion**

- LCS is an important example of **Dynamic Programming**.
- Offers a clear view of **optimal substructure** and **overlapping subproblems**.
- Useful in various real-world comparison and alignment problems.
