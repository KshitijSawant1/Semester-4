import java.util.*;

public class TicTacToeUserDriven {

    static final char PLAYER = 'X'; // Human
    static final char COMPUTER = 'O'; // AI
    static final char EMPTY = ' ';

    static char[][] board = {
        {EMPTY, EMPTY, EMPTY},
        {EMPTY, EMPTY, EMPTY},
        {EMPTY, EMPTY, EMPTY}
    };

    static Scanner scanner = new Scanner(System.in);

    static void printBoard(char[][] board) {
        System.out.println("Current Board:");
        for (char[] row : board) {
            System.out.println(Arrays.toString(row));
        }
        System.out.println();
    }

    static boolean isWinner(char[][] board, char player) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true;
            if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return true;
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true;
        return false;
    }

    static boolean isFull(char[][] board) {
        for (char[] row : board) {
            for (char cell : row) {
                if (cell == EMPTY) return false;
            }
        }
        return true;
    }

    static int minimax(char[][] board, boolean isMax) {
        if (isWinner(board, COMPUTER)) return 1;
        if (isWinner(board, PLAYER)) return -1;
        if (isFull(board)) return 0;

        int best = isMax ? Integer.MIN_VALUE : Integer.MAX_VALUE;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) {
                    board[i][j] = isMax ? COMPUTER : PLAYER;
                    int score = minimax(board, !isMax);
                    board[i][j] = EMPTY;
                    best = isMax ? Math.max(best, score) : Math.min(best, score);
                }
            }
        }
        return best;
    }

    static int[] findBestMove(char[][] board, char player) {
        int bestVal = player == COMPUTER ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        int[] bestMove = {-1, -1};

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) {
                    board[i][j] = player;
                    int moveVal = minimax(board, player == PLAYER);
                    board[i][j] = EMPTY;

                    if ((player == COMPUTER && moveVal > bestVal) || (player == PLAYER && moveVal < bestVal)) {
                        bestMove[0] = i;
                        bestMove[1] = j;
                        bestVal = moveVal;
                    }
                }
            }
        }
        return bestMove;
    }

    static void userMove() {
        while (true) {
            System.out.print("Enter your move (row and column: 0 0 to 2 2): ");
            int row = scanner.nextInt();
            int col = scanner.nextInt();
            if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == EMPTY) {
                board[row][col] = PLAYER;
                break;
            } else {
                System.out.println("Invalid move. Try again.");
            }
        }
    }

    static void computerMove() {
        int[] move = findBestMove(board, COMPUTER);
        if (move[0] != -1) {
            board[move[0]][move[1]] = COMPUTER;
            System.out.println("Computer chose position: (" + move[0] + ", " + move[1] + ")");
        }
    }

    public static void main(String[] args) {
        System.out.println("Welcome to Tic-Tac-Toe (User vs AI using Minimax)");
        printBoard(board);

        while (true) {
            userMove();
            printBoard(board);
            if (isWinner(board, PLAYER)) {
                System.out.println("Congratulations! You win!");
                break;
            }
            if (isFull(board)) {
                System.out.println("It's a draw!");
                break;
            }

            computerMove();
            printBoard(board);
            if (isWinner(board, COMPUTER)) {
                System.out.println("Computer wins!");
                break;
            }
            if (isFull(board)) {
                System.out.println("It's a draw!");
                break;
            }

            int[] nextBest = findBestMove(board, PLAYER);
            System.out.println("Suggested best move for you: (" + nextBest[0] + ", " + nextBest[1] + ")\n");
        }
    }
}
