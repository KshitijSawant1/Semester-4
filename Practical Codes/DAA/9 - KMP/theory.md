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