def print_board(board, N):
    for row in board:
        print(" ".join("Q" if col else "_" for col in row))
    print()

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, col, N, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack

def main():
    N = int(input("Enter the number of queens (N): "))
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_n_queens(board, 0, N, solutions)

    if not solutions:
        print("No solution exists for", N)
    else:
        print(f"\nTotal solutions for {N}-Queens: {len(solutions)}\n")
        for idx, sol in enumerate(solutions, 1):
            print(f"Solution {idx}:")
            print_board(sol, N)

if __name__ == "__main__":
    main()
