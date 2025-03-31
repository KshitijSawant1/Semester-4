def print_board(board):
    for row in board:
        print(row)
    print()

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, is_maximizing):
    if is_winner(board, 'X'):
        return 1
    elif is_winner(board, 'O'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for (i, j) in get_available_moves(board):
            board[i][j] = 'X'
            score = minimax(board, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for (i, j) in get_available_moves(board):
            board[i][j] = 'O'
            score = minimax(board, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = float('-inf')
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = 'X'
        score = minimax(board, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Initial board
board = [['X', 'O', 'X'],
         ['O', 'X', ' '],
         [' ', ' ', 'O']]

print("Current Board:")
print_board(board)

move = best_move(board)
print(f"Best move for X is at position: {move}")
board[move[0]][move[1]] = 'X'

print("Updated Board:")
print_board(board)
