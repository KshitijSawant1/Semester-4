def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row=0, board=[], solutions=[]):
    if row == n:
        solutions.append([''.join('Q' if i == c else ' - ' for i in range(n)) for c in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            solve_nqueens(n, row + 1, board + [col], solutions)
    return solutions

# ---- Main ----
n = int(input("Enter N: "))
results = solve_nqueens(n)
print(f"\nTotal solutions: {len(results)}")
for i, sol in enumerate(results, 1):
    print(f"\nSolution {i}:")
    for row in sol:
        print(row)
