## 🔧 Step 1: Compute LPS (Longest Prefix Suffix)

```python
def compute_lps(p):
```
Defines the function to compute the **LPS array** for the pattern `p`.

---

```python
    lps, length, i = [0]*len(p), 0, 1
```
- `lps`: list of length equal to the pattern, initialized with zeros.
- `length`: current length of the longest prefix suffix found so far.
- `i`: current index in the pattern (starts at 1 because `lps[0] = 0` by default).

---

```python
    while i < len(p):
```
Loop through the pattern to fill the `lps` array.

---

```python
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
```
If characters match at `i` and `length`, increment both `length` and `i`, and store the value of `length` in `lps[i]`.

---

```python
        elif length:
            length = lps[length-1]
```
If characters don't match and `length` is not zero, fall back to the previous LPS length without increasing `i`.

---

```python
        else:
            i += 1
```
If no prefix match, set `lps[i] = 0` (which is already done) and move to next index.

---

```python
    return lps
```
Returns the computed **LPS array**.

---

## 🔍 Step 2: KMP Search Function

```python
def kmp_search(t, p):
```
Defines the main function to perform **pattern matching** in text `t` using pattern `p`.

---

```python
    lps, res, i, j = compute_lps(p), [], 0, 0
```
- `lps`: compute the prefix table from the pattern
- `res`: list to store the starting indices of matches
- `i`: index for text
- `j`: index for pattern

---

```python
    while i < len(t):
```
Loop through the text while there's still characters left.

---

```python
        if t[i] == p[j]:
            i += 1
            j += 1
```
If characters match, increment both indices.

---

```python
        if j == len(p):
            res.append(i - j)
            j = lps[j - 1]
```
If the whole pattern is matched:
- Add the **starting index** of the match to `res`
- Use `lps` to reset `j` to continue searching for the next match

---

```python
        elif i < len(t) and t[i] != p[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
```
If characters don't match:
- If `j ≠ 0`, fallback using the `lps` table
- If `j = 0`, move to the next character in the text

---

```python
    return res
```
Return the list of indices where the pattern was found.

---

## 🖥️ Main Code Execution

```python
text = input("Enter text: ")
pattern = input("Enter pattern: ")
```
Take input from the user for text and pattern.

---

```python
result = kmp_search(text, pattern)
```
Call the KMP search function.

---

```python
print("\nPattern found at:", result if result else "No match")
```
Print the result — list of starting indices, or "No match" if the result is empty.

---

## 🧾 Example Run

**Input:**
```
Enter text: ABCDABABCABCDABCDABDE
Enter pattern: ABCDABD
```

**Output:**
```
Pattern found at: [15]
```

---

## ✅ Summary:
- `compute_lps()` preprocesses the pattern to avoid rechecking characters
- `kmp_search()` performs the efficient string match in **O(n + m)** time
- Compact and elegant with minimal variables and clean logic
---

### ✅ **KMP Algorithm Analysis Table**

| **Aspect**            | **Complexity**       | **Reason / Explanation**                                                                 |
|------------------------|----------------------|--------------------------------------------------------------------------------------------|
| **Best Case**           | **O(n)**             | Pattern matches immediately or mismatches occur early, causing minimal backtracking.       |
| **Average Case**        | **O(n)**             | Efficient prefix table (LPS) helps skip rechecking characters during mismatches.           |
| **Worst Case**          | **O(n)**             | Even in worst-case patterns (like repeated chars), the algorithm performs at most `2n−1` steps. |
| **Preprocessing Time**  | **O(m)**             | LPS (Longest Prefix Suffix) array computation for the pattern takes linear time.           |
| **Space Complexity**    | **O(m)**             | Stores the LPS array of size equal to the length of the pattern.                           |

---

### 🔍 Explanation:

#### 🔹 Time Complexity

- **n** = length of the text  
- **m** = length of the pattern  

KMP avoids rechecking characters in the text by using the **LPS array**, which ensures **no character is checked more than twice**.

- Best/Average/Worst: **O(n)**  
- LPS construction: **O(m)**  
  So total: **O(n + m)** in all cases

#### 🔹 Best Case
- Characters mismatch early → quick skips using LPS → linear scans.

#### 🔹 Worst Case
- Pattern like `"AAAAA"` in text `"AAAAAAAAAA"`: KMP still performs linear scans thanks to LPS guidance.

#### 🔹 Space Complexity
- LPS array of size **m** → **O(m)** space
- No extra memory for stack or recursion

---

### ✅ Summary Table

| **Metric**               | **Complexity** | **Explanation**                                                                      |
|--------------------------|----------------|---------------------------------------------------------------------------------------|
| **Time (Best)**           | O(n)           | Immediate match/mismatch with minimal comparisons                                    |
| **Time (Average)**        | O(n)           | Efficient LPS allows skipping redundant checks during mismatches                     |
| **Time (Worst)**          | O(n)           | Pattern overlaps itself; even then, no rechecking due to precomputed LPS             |
| **Preprocessing Time**    | O(m)           | LPS array creation takes time linear to the pattern length                           |
| **Space**                 | O(m)           | Stores only the LPS array of length m                                                |

---
**comparison table of four popular string matching algorithms**:

- **Naive**
- **Rabin-Karp**
- **Boyer-Moore**
- **KMP (Knuth-Morris-Pratt)**

This includes their **approach**, **time and space complexities**, and **key strengths/limitations**.

---

### ✅ **String Matching Algorithms – Comparison Table**

| **Feature**              | **Naive**                  | **Rabin-Karp**              | **Boyer-Moore**                | **KMP (Knuth-Morris-Pratt)**       |
|--------------------------|----------------------------|-----------------------------|-------------------------------|-------------------------------------|
| **Approach**             | Brute force character-by-character check | Hash-based rolling comparison | Right-to-left matching with skip tables | Prefix function with LPS (Longest Prefix Suffix) |
| **Preprocessing Time**   | O(1)                       | O(1) or O(m)                | O(m + alphabet_size)          | O(m)                                |
| **Best Case Time**       | O(m + n)                   | O(m + n)                    | **O(n / m)**                   | O(n)                                |
| **Average Case Time**    | O((n − m + 1) × m)         | O(n + m)                    | O(n)                          | O(n)                                |
| **Worst Case Time**      | O((n − m + 1) × m)         | **O(n × m)** (with poor hashes) | O(n + m) (with good heuristics) | O(n + m)                            |
| **Space Complexity**     | O(1)                       | O(1) or O(m)                | O(m + alphabet size)          | O(m)                                |
| **Handles Overlapping Patterns** | Yes              | Yes                         | Not optimal for overlapping   | Yes                                 |
| **Handles Mismatches Well**     | No               | No                          | Yes (via bad character & good suffix) | Yes (via LPS)                   |
| **Best For**             | Simplicity, small inputs   | Searching **multiple patterns** or plagiarism detection | Large texts with small patterns | Fast linear-time search with pattern reuse |
| **Drawbacks**            | Very slow for large texts  | Hash collisions can cause worst-case | Complex to implement fully    | LPS preprocessing can be tricky     |

---

### 📌 Notation:
- `n` = length of text  
- `m` = length of pattern  

---

### 🧠 Quick Takeaways:

- **Naive**: Simple but inefficient; useful for small data or educational purposes.
- **Rabin-Karp**: Good for **multiple pattern matching**; depends on hash quality.
- **Boyer-Moore**: Very fast in practice (especially with long alphabets); **skips many characters**.
- **KMP**: Excellent worst-case performance; efficient **prefix-aware pattern matching**.

---