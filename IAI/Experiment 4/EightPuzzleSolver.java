import java.util.*;

class PuzzleState {
    int[][] board;
    String path;
    int emptyRow, emptyCol;

    // Constructor
    public PuzzleState(int[][] board, String path, int emptyRow, int emptyCol) {
        this.board = board;
        this.path = path;
        this.emptyRow = emptyRow;
        this.emptyCol = emptyCol;
    }

    // Check if current state is equal to goal state
    public boolean isGoalState(int[][] goal) {
        return Arrays.deepEquals(this.board, goal);
    }

    // Generate possible moves from the current state
    public List<PuzzleState> generateNextStates() {
        List<PuzzleState> nextStates = new ArrayList<>();
        int[] dx = {-1, 1, 0, 0};  // Up, Down, Left, Right
        int[] dy = {0, 0, -1, 1};
        String[] moves = {"U", "D", "L", "R"};

        for (int i = 0; i < 4; i++) {
            int newRow = emptyRow + dx[i];
            int newCol = emptyCol + dy[i];

            if (newRow >= 0 && newRow < 3 && newCol >= 0 && newCol < 3) {
                int[][] newBoard = copyBoard(this.board);
                // Swap blank space
                newBoard[emptyRow][emptyCol] = newBoard[newRow][newCol];
                newBoard[newRow][newCol] = 0;

                nextStates.add(new PuzzleState(newBoard, this.path + moves[i], newRow, newCol));
            }
        }

        return nextStates;
    }

    private int[][] copyBoard(int[][] board) {
        int[][] newBoard = new int[3][3];
        for (int i = 0; i < 3; i++) {
            newBoard[i] = board[i].clone();
        }
        return newBoard;
    }

    // Convert board to string (for visited states)
    @Override
    public int hashCode() {
        return Arrays.deepHashCode(board);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof PuzzleState) {
            return Arrays.deepEquals(this.board, ((PuzzleState) obj).board);
        }
        return false;
    }

    // Utility function to print the board with path
    public void printBoard() {
        System.out.println("Path so far: " + (path.isEmpty() ? "Initial State" : path));
        for (int[] row : board) {
            for (int cell : row) {
                System.out.print((cell == 0 ? " " : cell) + " ");
            }
            System.out.println();
        }
        System.out.println("--------------------");
    }
}

public class EightPuzzleSolver {
    // Perform BFS (Uninformed Search)
    public static void bfs(int[][] initial, int[][] goal) {
        Queue<PuzzleState> queue = new LinkedList<>();
        Set<PuzzleState> visited = new HashSet<>();

        int emptyRow = -1, emptyCol = -1;
        // Find the blank space
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (initial[i][j] == 0) {
                    emptyRow = i;
                    emptyCol = j;
                    break;
                }
            }
        }

        PuzzleState startState = new PuzzleState(initial, "", emptyRow, emptyCol);
        queue.add(startState);
        visited.add(startState);

        while (!queue.isEmpty()) {
            PuzzleState currentState = queue.poll();
            currentState.printBoard(); // Print the current board state

            // Goal test
            if (currentState.isGoalState(goal)) {
                System.out.println("✅ Solution found with path: " + currentState.path);
                currentState.printBoard();
                return;
            }

            // Generate next moves
            for (PuzzleState nextState : currentState.generateNextStates()) {
                if (!visited.contains(nextState)) {
                    queue.add(nextState);
                    visited.add(nextState);
                }
            }
        }

        System.out.println("❌ No solution found.");
    }

    // Main function
    public static void main(String[] args) {
        // Initial State
        int[][] initial = {
            {1, 4, 3},
            {2, 5, 6},
            {8, 7, 0}
        };

        // Goal State
        int[][] goal = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 0}
        };

        System.out.println("Solving 8-puzzle problem using BFS (Uninformed Search):\n");
        bfs(initial, goal);
    }
}
