Here’s a detailed explanation and analysis of solving the **8-Queens Problem using Backtracking**:

---

### 🔍 **Introduction:**
The **8-Queens Problem** is a classic **constraint satisfaction** and **backtracking** problem.  
The goal is to place 8 queens on an 8×8 chessboard so that no two queens threaten each other.  
This means:
- No two queens share the same row
- No two queens share the same column
- No two queens share the same diagonal

---

### ✅ **Algorithm (Step-by-Step - Backtracking):**
1. Start from the leftmost column (column = 0).
2. For each row in the current column:
   - Check if placing a queen at `[row][col]` is **safe**.
   - If **safe**, place the queen and move to the next column recursively.
   - If placing leads to a valid configuration, return `True`.
   - Else, **backtrack** by removing the queen from the current cell and trying the next row.
3. If no safe row is found in the current column, return `False` (trigger backtracking).

---

### 💡 **Pseudocode:**
```
function solveNQueens(board, col):
    if col >= N:
        return True

    for row from 0 to N-1:
        if isSafe(board, row, col):
            board[row][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[row][col] = 0  // backtrack
    return False
```

**isSafe(board, row, col)** checks:
- Same row to the left
- Upper-left diagonal
- Lower-left diagonal

---

### 🧠 **Working Example:**

Start with column 0:  
Try placing the queen in rows 0 to 7.  
For each valid placement, recursively solve for the next column.

If a column cannot place any queen safely, backtrack to the previous column and try a different row.

Continue until all 8 queens are placed or all options are exhausted.

---

### 🔁 **Recurrence Relation:**
At each step, we try at most **N rows** for **N columns**, and call the function recursively.

```
T(N) = N * T(N - 1) + O(N)
```

But since we backtrack when unsafe, **not all branches are explored**, which makes it much faster in practice.

---

### ⏱ **Time Complexity:**
- **Worst-case:** O(N!)  
- **Average-case (with pruning/backtracking):** Better than O(N!), but still exponential  
- **Space Complexity:** O(N²) for board + O(N) for recursion stack

---

### 📈 **Case Complexity:**
| Case         | Description                            | Time        |
|--------------|----------------------------------------|-------------|
| Best Case    | First valid solution found early       | O(N²)       |
| Worst Case   | All permutations checked               | O(N!)       |
| Average Case | Depends on pruning efficiency          | < O(N!)     |

---

### ✅ **Conclusion:**
The 8-Queens Problem demonstrates how **backtracking** can efficiently explore solution spaces by **pruning** invalid paths.  
It avoids brute force by eliminating unsafe positions early, making it a powerful method in constraint-solving scenarios.

Here is the **Python code** to solve the **8-Queens Problem using the Backtracking Approach** with a clean output display of the solution board:

---

### ✅ **Python Code:**

```python
N = 8  # You can change N for N-Queens

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    # Check row on left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens(board, col):
    if col >= N:
        print("✅ One of the solutions:")
        print_board(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = 0  # Backtrack

    return res

# Driver code
board = [[0 for _ in range(N)] for _ in range(N)]
if not solve_n_queens(board, 0):
    print("❌ No solution exists")
```

---

### 📌 **How It Works:**
- `board`: Keeps track of queen placements.
- `is_safe`: Validates queen placement based on chess rules.
- `solve_n_queens`: Core backtracking logic.
- The board is printed with `Q` representing queens and `.` representing empty cells.

---
