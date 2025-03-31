import java.util.*;

class PuzzleNode implements Comparable<PuzzleNode> {
    int[][] state;
    int g; // Cost so far
    int h; // Heuristic
    List<int[][]> path;

    PuzzleNode(int[][] state, int g, int h, List<int[][]> path) {
        this.state = state;
        this.g = g;
        this.h = h;
        this.path = new ArrayList<>(path);
        this.path.add(copyState(state));
    }

    public int f() {
        return g + h;
    }

    @Override
    public int compareTo(PuzzleNode other) {
        return Integer.compare(this.f(), other.f());
    }

    private int[][] copyState(int[][] original) {
        int[][] copy = new int[3][3];
        for (int i = 0; i < 3; i++)
            System.arraycopy(original[i], 0, copy[i], 0, 3);
        return copy;
    }
}

public class AStarEightPuzzle {

    static int[][] goal = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 0}
    };

    static int heuristic(int[][] state) {
        int dist = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int val = state[i][j];
                if (val != 0) {
                    int goalX = (val - 1) / 3;
                    int goalY = (val - 1) % 3;
                    dist += Math.abs(i - goalX) + Math.abs(j - goalY);
                }
            }
        }
        return dist;
    }

    static int[] findZero(int[][] state) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (state[i][j] == 0) return new int[]{i, j};
            }
        }
        return null;
    }

    static List<int[][]> getNeighbors(int[][] state) {
        List<int[][]> neighbors = new ArrayList<>();
        int[] blank = findZero(state);
        int x = blank[0], y = blank[1];
        int[][] moves = {{-1,0},{1,0},{0,-1},{0,1}};

        for (int[] move : moves) {
            int nx = x + move[0];
            int ny = y + move[1];
            if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                int[][] newState = copyState(state);
                newState[x][y] = newState[nx][ny];
                newState[nx][ny] = 0;
                neighbors.add(newState);
            }
        }
        return neighbors;
    }

    static int[][] copyState(int[][] state) {
        int[][] copy = new int[3][3];
        for (int i = 0; i < 3; i++)
            System.arraycopy(state[i], 0, copy[i], 0, 3);
        return copy;
    }

    static boolean isGoal(int[][] state) {
        return Arrays.deepEquals(state, goal);
    }

    static void solve(int[][] initial) {
        PriorityQueue<PuzzleNode> openSet = new PriorityQueue<>();
        Set<String> visited = new HashSet<>();

        openSet.add(new PuzzleNode(initial, 0, heuristic(initial), new ArrayList<>()));

        while (!openSet.isEmpty()) {
            PuzzleNode current = openSet.poll();

            if (isGoal(current.state)) {
                int step = 0;
                for (int[][] board : current.path) {
                    int h = heuristic(board);
                    int g = step;
                    int f = g + h;
                    System.out.println("Step " + step + " : g(n)=" + g + ", h(n)=" + h + ", f(n)=" + f);
                    for (int[] row : board) System.out.println(Arrays.toString(row));
                    System.out.println();
                    step++;
                }
                return;
            }

            visited.add(Arrays.deepToString(current.state));

            for (int[][] neighbor : getNeighbors(current.state)) {
                if (!visited.contains(Arrays.deepToString(neighbor))) {
                    openSet.add(new PuzzleNode(neighbor, current.g + 1, heuristic(neighbor), current.path));
                }
            }
        }
        System.out.println("No solution found.");
    }

    public static void main(String[] args) {
        int[][] initial = {
            {1, 4, 3},
            {2, 5, 6},
            {8, 7, 0}
        };

        solve(initial);
    }
}
