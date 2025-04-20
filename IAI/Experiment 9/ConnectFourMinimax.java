import java.util.*;

public class ConnectFourMinimax {

    static final int ROWS = 4;
    static final int COLS = 4;
    static final char EMPTY = '-';
    static final char PLAYER = 'O'; // Human
    static final char AI = 'X';     // AI

    static char[][] board = new char[ROWS][COLS];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        initializeBoard();

        printBoard();
        while (true) {
            System.out.print("Enter your move (0-3): ");
            int col = scanner.nextInt();
            if (!makeMove(col, PLAYER)) {
                System.out.println("Invalid move! Try again.");
                continue;
            }

            printBoard();
            if (checkWin(PLAYER)) {
                System.out.println("You win!");
                break;
            }
            if (isBoardFull()) {
                System.out.println("It's a draw!");
                break;
            }

            System.out.println("AI is thinking...");
            int bestMove = findBestMove();
            makeMove(bestMove, AI);
            printBoard();

            if (checkWin(AI)) {
                System.out.println("AI wins!");
                break;
            }
            if (isBoardFull()) {
                System.out.println("It's a draw!");
                break;
            }
        }
        scanner.close();
    }

    static void initializeBoard() {
        for (int i = 0; i < ROWS; i++)
            Arrays.fill(board[i], EMPTY);
    }

    static void printBoard() {
        for (char[] row : board) {
            for (char cell : row)
                System.out.print(cell + " ");
            System.out.println();
        }
        System.out.println("0 1 2 3");
    }

    static boolean makeMove(int col, char player) {
        if (col < 0 || col >= COLS || board[0][col] != EMPTY)
            return false;

        for (int i = ROWS - 1; i >= 0; i--) {
            if (board[i][col] == EMPTY) {
                board[i][col] = player;
                return true;
            }
        }
        return false;
    }

    static void undoMove(int col) {
        for (int i = 0; i < ROWS; i++) {
            if (board[i][col] != EMPTY) {
                board[i][col] = EMPTY;
                break;
            }
        }
    }

    static boolean isBoardFull() {
        for (int i = 0; i < COLS; i++) {
            if (board[0][i] == EMPTY)
                return false;
        }
        return true;
    }

    static boolean checkWin(char player) {
        // Check rows and columns
        for (int i = 0; i < ROWS; i++)
            for (int j = 0; j < COLS - 3; j++)
                if (board[i][j] == player && board[i][j+1] == player &&
                    board[i][j+2] == player && board[i][j+3] == player)
                    return true;

        for (int j = 0; j < COLS; j++)
            for (int i = 0; i < ROWS - 3; i++)
                if (board[i][j] == player && board[i+1][j] == player &&
                    board[i+2][j] == player && board[i+3][j] == player)
                    return true;

        // Check diagonals
        for (int i = 0; i < ROWS - 3; i++)
            for (int j = 0; j < COLS - 3; j++)
                if (board[i][j] == player && board[i+1][j+1] == player &&
                    board[i+2][j+2] == player && board[i+3][j+3] == player)
                    return true;

        for (int i = 3; i < ROWS; i++)
            for (int j = 0; j < COLS - 3; j++)
                if (board[i][j] == player && board[i-1][j+1] == player &&
                    board[i-2][j+2] == player && board[i-3][j+3] == player)
                    return true;

        return false;
    }

    static int evaluateBoard() {
        if (checkWin(AI))
            return 10;
        else if (checkWin(PLAYER))
            return -10;
        else
            return 0;
    }

    static int minimax(int depth, boolean isMax, int alpha, int beta) {
        int score = evaluateBoard();
        if (score == 10 || score == -10 || isBoardFull())
            return score;

        if (isMax) {
            int best = Integer.MIN_VALUE;
            for (int col = 0; col < COLS; col++) {
                if (makeMove(col, AI)) {
                    best = Math.max(best, minimax(depth + 1, false, alpha, beta));
                    undoMove(col);
                    alpha = Math.max(alpha, best);
                    if (beta <= alpha) break;
                }
            }
            return best;
        } else {
            int best = Integer.MAX_VALUE;
            for (int col = 0; col < COLS; col++) {
                if (makeMove(col, PLAYER)) {
                    best = Math.min(best, minimax(depth + 1, true, alpha, beta));
                    undoMove(col);
                    beta = Math.min(beta, best);
                    if (beta <= alpha) break;
                }
            }
            return best;
        }
    }

    static int findBestMove() {
        int bestVal = Integer.MIN_VALUE;
        int bestMove = -1;

        for (int col = 0; col < COLS; col++) {
            if (makeMove(col, AI)) {
                int moveVal = minimax(0, false, Integer.MIN_VALUE, Integer.MAX_VALUE);
                undoMove(col);

                if (moveVal > bestVal) {
                    bestVal = moveVal;
                    bestMove = col;
                }
            }
        }
        return bestMove;
    }
}
