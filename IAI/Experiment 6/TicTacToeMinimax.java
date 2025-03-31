import java.util.*;

public class TicTacToeMinimax {

    static final char PLAYER = 'X'; // Maximizing player
    static final char OPPONENT = 'O'; // Minimizing player
    static final char EMPTY = ' ';

    static char[][] board = {
        {'X', 'O', 'X'},
        {'O', 'X', ' '},
        {' ', ' ', 'O'}
    };

    // Print the board
    static void printBoard(char[][] board) {
        for (char[] row : board) {
            System.out.println(Arrays.toString(row));
        }
        System.out.println();
    }

    // Check if a player has won
    static boolean isWinner(char[][] board, char player) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true;
            if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return true;
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true;
        return false;
    }

    // Check if the board is full
    static boolean isFull(char[][] board) {
        for (char[] row : board) {
            for (char cell : row) {
                if (cell == EMPTY) return false;
            }
        }
        return true;
    }

    // Minimax Algorithm
    static int minimax(char[][] board, boolean isMax) {
        if (isWinner(board, PLAYER)) return 1;
        if (isWinner(board, OPPONENT)) return -1;
        if (isFull(board)) return 0;

        int best = isMax ? Integer.MIN_VALUE : Integer.MAX_VALUE;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) {
                    board[i][j] = isMax ? PLAYER : OPPONENT;
                    int score = minimax(board, !isMax);
                    board[i][j] = EMPTY;
                    best = isMax ? Math.max(best, score) : Math.min(best, score);
                }
            }
        }
        return best;
    }

    // Find best move for 'X'
    static int[] findBestMove(char[][] board) {
        int bestVal = Integer.MIN_VALUE;
        int[] bestMove = {-1, -1};

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) {
                    board[i][j] = PLAYER;
                    int moveVal = minimax(board, false);
                    board[i][j] = EMPTY;

                    if (moveVal > bestVal) {
                        bestMove[0] = i;
                        bestMove[1] = j;
                        bestVal = moveVal;
                    }
                }
            }
        }
        return bestMove;
    }

    public static void main(String[] args) {
        System.out.println("Current Board:");
        printBoard(board);

        int[] move = findBestMove(board);
        if (move[0] != -1) {
            board[move[0]][move[1]] = PLAYER;
            System.out.println("Best move for X is at position: (" + move[0] + ", " + move[1] + ")");
        } else {
            System.out.println("No moves available.");
        }

        System.out.println("Updated Board:");
        printBoard(board);
    }
}
