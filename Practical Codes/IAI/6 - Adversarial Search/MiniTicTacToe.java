import java.util.*;

public class MiniTicTacToe {
    static char[][] b = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    static Scanner sc = new Scanner(System.in);

    static boolean win(char p) {
        for (int i = 0; i < 3; i++)
            if ((b[i][0] == p && b[i][1] == p && b[i][2] == p) || (b[0][i] == p && b[1][i] == p && b[2][i] == p)) return true;
        return (b[0][0] == p && b[1][1] == p && b[2][2] == p) || (b[0][2] == p && b[1][1] == p && b[2][0] == p);
    }

    static boolean full() {
        for (char[] r : b) for (char c : r) if (c == ' ') return false;
        return true;
    }

    static int minimax(boolean max) {
        if (win('X')) return 10;
        if (win('O')) return -10;
        if (full()) return 0;
        int best = max ? -1000 : 1000;
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++)
            if (b[i][j] == ' ') {
                b[i][j] = max ? 'X' : 'O';
                int score = minimax(!max);
                b[i][j] = ' ';
                best = max ? Math.max(best, score) : Math.min(best, score);
            }
        return best;
    }

    static void computerMove() {
        int bestVal = -1000, bi = 0, bj = 0;
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++)
            if (b[i][j] == ' ') {
                b[i][j] = 'X';
                int val = minimax(false);
                b[i][j] = ' ';
                if (val > bestVal) {
                    bestVal = val;
                    bi = i;
                    bj = j;
                }
            }
        b[bi][bj] = 'X';
        System.out.println("Computer placed X at (" + bi + "," + bj + ")");
    }

    static void printBoard() {
        for (char[] r : b) System.out.println(Arrays.toString(r));
    }

    public static void main(String[] args) {
        System.out.println("Play Tic Tac Toe (You = O, Computer = X)");
        while (true) {
            printBoard();
            if (win('X')) { System.out.println("Computer wins!"); break; }
            if (win('O')) { System.out.println("You win!"); break; }
            if (full())   { System.out.println("Draw!"); break; }

            int r, c;
            do {
                System.out.print("Your move (row col 0-2): ");
                r = sc.nextInt(); c = sc.nextInt();
            } while (r < 0 || r > 2 || c < 0 || c > 2 || b[r][c] != ' ');
            b[r][c] = 'O';
            if (!win('O') && !full()) computerMove();
        }
        printBoard();
    }
}
