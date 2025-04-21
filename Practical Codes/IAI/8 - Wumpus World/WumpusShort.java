import java.util.*;

public class WumpusShort {
    static String[][] world = {
        {"Stench", "", "Breeze", "PIT"},
        {"Wumpus", "Breeze,Stench,Gold", "PIT", "Breeze"},
        {"Stench", "Breeze", "", ""},
        {"START", "Breeze", "PIT", "Breeze"}
    };
    static boolean[][] visited = new boolean[4][4];
    static int x = 3, y = 0;
    static boolean alive = true, gold = false;

    static void menu() {
        System.out.println("\n1.Up 2.Down 3.Left 4.Right 5.Sense 6.Grab 7.Exit");
    }

    static void view() {
        for (int i = 0; i < 4; i++, System.out.println())
            for (int j = 0; j < 4; j++)
                System.out.print(i == x && j == y ? " A " : visited[i][j] ? (world[i][j].contains("Gold") && !gold ? " G " : " . ") : " * ");
    }

    static void sense() {
        String tile = world[x][y];
        visited[x][y] = true;
        if (tile.contains("PIT")) {
            System.out.println("Fell in PIT!"); alive = false;
        } else if (tile.contains("Wumpus")) {
            System.out.println("Eaten by Wumpus!"); alive = false;
        } else {
            if (tile.contains("Stench")) System.out.println("Stench nearby.");
            if (tile.contains("Breeze")) System.out.println("Breeze nearby.");
            if (tile.contains("Gold")) System.out.println("Gold is here!");
            if (tile.equals("")) System.out.println("Safe here.");
        }
    }

    static void move(int dx, int dy) {
        int nx = x + dx, ny = y + dy;
        if (nx >= 0 && ny >= 0 && nx < 4 && ny < 4) {
            x = nx; y = ny;
            System.out.println("Moved to (" + x + "," + y + ")");
            sense();
        } else System.out.println("Hit a wall.");
    }

    static void grab() {
        if (world[x][y].contains("Gold")) {
            gold = true;
            world[x][y] = world[x][y].replace("Gold", "").trim();
            System.out.println("Gold grabbed! Return to (3,0).");
        } else System.out.println("No gold here.");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Wumpus World 4x4 — Start at (3,0). Avoid PITs and Wumpus!");
        visited[x][y] = true; sense();

        while (alive) {
            if (gold && x == 3 && y == 0) { System.out.println("YOU WIN!"); break; }
            view(); menu();
            switch (sc.nextInt()) {
                case 1 -> move(-1, 0); case 2 -> move(1, 0);
                case 3 -> move(0, -1); case 4 -> move(0, 1);
                case 5 -> sense(); case 6 -> grab();
                case 7 -> { System.out.println("Goodbye."); return; }
                default -> System.out.println("Invalid!");
            }
        }
        if (!alive) System.out.println("You DIED!");
        sc.close();
    }
}
