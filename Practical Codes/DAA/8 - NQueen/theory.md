### 🔷 `is_safe()` – Check if it's safe to place a queen at (row, col)

```python
def is_safe(board, row, col, n):
```
Defines a function to check whether placing a queen at position `(row, col)` is safe, given the current state of the board.

```python
    for i in range(row):
```
Loop over all previously placed rows (because queens are placed one per row from top to bottom).

```python
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
```

This line checks **three attack directions** from previously placed queens:
- `board[i] == col` → **Same column**
- `board[i] - i == col - row` → **Left diagonal** (i.e., `/`)
- `board[i] + i == col + row` → **Right diagonal** (i.e., `\`)

If any of these are true, the queen at `(row, col)` can be **attacked**, so it's not safe.

```python
    return True
```
If none of the above conditions triggered, the position is safe.

---

### 🔷 `solve_nqueens()` – Recursive backtracking to find all solutions

```python
def solve_nqueens(n, row=0, board=[], solutions=[]):
```
Defines the recursive function:
- `n`: size of the board (N x N)
- `row`: current row we’re placing a queen in
- `board`: list storing column indices of placed queens (1 per row)
- `solutions`: list of all valid board solutions

---

```python
    if row == n:
```
If we've placed a queen on all `n` rows, we’ve found a complete solution.

```python
        solutions.append([''.join('Q' if i == c else ' - ' for i in range(n)) for c in board])
```
- Builds a visual representation of the board using list comprehension:
  - For each row `c` (which stores queen's column position),
  - Place `'Q'` at the column `i == c` and `' - '` elsewhere.
- Appends this formatted board to the `solutions` list.

```python
        return
```
End the current recursive path since the board is complete.

---

```python
    for col in range(n):
```
Try placing a queen in each column of the current row.

```python
        if is_safe(board, row, col, n):
```
Only proceed if placing a queen at `(row, col)` is safe.

```python
            solve_nqueens(n, row + 1, board + [col], solutions)
```
- Place the queen in column `col` by adding `col` to the `board` list.
- Move to the next row (`row + 1`) recursively.
- `board + [col]` creates a **new list** (so we don't modify the original during backtracking).

```python
    return solutions
```
After checking all possibilities, return the list of valid solutions.

---

### 🔷 Main Program

```python
n = int(input("Enter N: "))
```
Take user input for the board size (N x N).

---

```python
results = solve_nqueens(n)
```
Call the function to compute all valid placements of N queens.

---

```python
print(f"\nTotal solutions: {len(results)}")
```
Print the total number of distinct solutions found.

---

```python
for i, sol in enumerate(results, 1):
    print(f"\nSolution {i}:")
    for row in sol:
        print(row)
```
- Loop through all solutions.
- For each solution:
  - Print a readable chessboard.
  - `row` is already a string like: `' -  Q -  - '`.

---

### 🧾 Example Output (N = 4)
```
Total solutions: 2

Solution 1:
 -  Q -  - 
 -  -  -  Q
Q -  -  - 
 -  -  Q - 

Solution 2:
 -  -  Q - 
Q -  -  - 
 -  -  -  Q
 -  Q -  - 
```

---

### ✅ Summary
- **Efficiently places queens** using backtracking.
- Uses a **list of column positions (`board`)** instead of a full matrix.
- Checks **three directions**: vertical, diagonal left (`/`), and diagonal right (`\`).
- Builds and stores each complete solution in a readable format.
