import java.util.*;

public class TicTacToeMini {
    static char[][] b = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    static Scanner sc = new Scanner(System.in);

    static int eval() {
        for (int i = 0; i < 3; i++) {
            if (b[i][0] == b[i][1] && b[i][1] == b[i][2]) return b[i][0] == 'X' ? 10 : b[i][0] == 'O' ? -10 : 0;
            if (b[0][i] == b[1][i] && b[1][i] == b[2][i]) return b[0][i] == 'X' ? 10 : b[0][i] == 'O' ? -10 : 0;
        }
        if (b[0][0] == b[1][1] && b[1][1] == b[2][2]) return b[0][0] == 'X' ? 10 : b[0][0] == 'O' ? -10 : 0;
        if (b[0][2] == b[1][1] && b[1][1] == b[2][0]) return b[0][2] == 'X' ? 10 : b[0][2] == 'O' ? -10 : 0;
        return 0;
    }

    static boolean movesLeft() {
        for (char[] r : b) for (char c : r) if (c == ' ') return true;
        return false;
    }

    static int minimax(boolean max, int alpha, int beta) {
        int score = eval();
        if (score != 0 || !movesLeft()) return score;

        int best = max ? -1000 : 1000;
        for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++)
            if (b[i][j] == ' ') {
                b[i][j] = max ? 'X' : 'O';
                int val = minimax(!max, alpha, beta);
                b[i][j] = ' ';
                best = max ? Math.max(best, val) : Math.min(best, val);
                if (max) alpha = Math.max(alpha, best); else beta = Math.min(beta, best);
                if (beta <= alpha) return best;
            }
        return best;
    }
    static int[] bestMove() {
        int best = -1000;
        int[] move = {-1, -1};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (b[i][j] == ' ') {
                    b[i][j] = 'X';
                    int val = minimax(false, -1000, 1000);
                    b[i][j] = ' ';
                    if (val > best) {
                        best = val;
                        move = new int[]{i, j};
                    }
                }
            }
        }
        return move;
    }
    

    static void print() { for (char[] r : b) System.out.println(Arrays.toString(r)); }

    public static void main(String[] args) {
        System.out.println("Tic Tac Toe: You=O, AI=X");
        while (true) {
            print();
            if (eval() == 10) { System.out.println("AI wins!"); break; }
            if (eval() == -10) { System.out.println("You win!"); break; }
            if (!movesLeft()) { System.out.println("Draw!"); break; }

            int r, c;
            do {
                System.out.print("Your move (row col): ");
                r = sc.nextInt(); c = sc.nextInt();
            } while (r < 0 || r > 2 || c < 0 || c > 2 || b[r][c] != ' ');
            b[r][c] = 'O';

            if (movesLeft() && eval() == 0) {
                int[] m = bestMove();
                b[m[0]][m[1]] = 'X';
                System.out.println("AI played at (" + m[0] + "," + m[1] + ")");
            }
        }
        print();
    }
}
