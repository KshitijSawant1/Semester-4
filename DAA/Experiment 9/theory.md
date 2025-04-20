Here is the complete explanation and Python code implementation for **Experiment 09 – Knuth-Morris-Pratt (KMP) Algorithm** including menu-driven interaction and a sample execution:

---

## ✅ **Experiment 09 – KMP String Matching Algorithm**

### 🎯 **Learning Objective:**
- Understand the working and logic behind the **KMP (Knuth-Morris-Pratt) algorithm**.
- Develop code to perform **efficient pattern matching**.

---

### 🔍 **Theory Overview:**

The **KMP Algorithm** is an efficient string-matching algorithm that avoids unnecessary comparisons using a **precomputed prefix table**.

---

### 🔧 **Components of KMP Algorithm:**

1. **Prefix Function (Π Table)**  
   - Helps to **skip characters** while matching after a mismatch.
   - Stores the **length of the longest prefix** which is also a suffix for each sub-pattern.

2. **KMP Matcher**  
   - Uses the prefix function to efficiently search for the **pattern `P` in the text `T`**.

---

### 💡 **Algorithm Steps:**

#### **Prefix Function:**
```python
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi
```

#### **KMP Matcher:**
```python
def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0
    occurrences = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]
    return occurrences
```

---

### 📋 **Menu-Driven Python Code:**
```python
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0
    occurrences = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]
    return occurrences

def main():
    while True:
        print("\n===== KMP String Matching Algorithm =====")
        print("1. Run with default input")
        print("2. Run with custom input")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = "ABABDABACDABABCABAB"
            pattern = "ABABCABAB"
        elif choice == '2':
            text = input("Enter the text string: ")
            pattern = input("Enter the pattern string: ")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        print(f"\nText     : {text}")
        print(f"Pattern  : {pattern}")
        matches = kmp_matcher(text, pattern)

        if matches:
            print("Pattern found at positions:", matches)
        else:
            print("Pattern not found.")

if __name__ == "__main__":
    main()
```

---

### ✅ **Sample Execution:**

**Default Input:**
```
Text     : ABABDABACDABABCABAB
Pattern  : ABABCABAB
Pattern found at positions: [10]
```

**Custom Input:**
```
Text     : AABAACAADAABAABA
Pattern  : AABA
Pattern found at positions: [0, 9, 12]
```

---

### 📚 **Learning Outcome:**
- Understood how **KMP uses prefix table** to avoid rechecking characters.
- Efficiently implemented the logic in Python with **real-world applications** like search engines, text editors, and DNA sequence analysis.

---

### 📌 **Conclusion:**
The KMP algorithm is a powerful tool for fast and efficient pattern matching. Its linear time complexity makes it suitable for **large-scale text processing** and **pattern searching** tasks.

Would you like a **C or Java version** of the same as well?