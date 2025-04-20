import java.util.Scanner;

public class WumpusWorld {

    static String[][] world = {
        {"Safe", "Breeze , Stench", "Pit", "Breeze"},
        {"Stench", "Wumpus", "Breeze , Stench", "Safe"},
        {"Safe", "stench", "Safe", "Glitter"},
        {"Safe", "Safe", "Safe", "Safe"}
    };

    static boolean[][] visited = new boolean[4][4];
    static int x = 0, y = 0;
    static boolean hasGold = false;
    static boolean isAlive = true;

    static void displayMenu() {
        System.out.println("\n=== Wumpus World Menu ===");
        System.out.println("1. Move Up");
        System.out.println("2. Move Down");
        System.out.println("3. Move Left");
        System.out.println("4. Move Right");
        System.out.println("5. Sense Environment");
        System.out.println("6. Grab Gold");
        System.out.println("7. Exit Game");
        System.out.print("Choose an option: ");
    }

    static void printWorldView() {
        System.out.println("\nCurrent World View:");
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (i == x && j == y) {
                    System.out.print(" A ");
                } else if (visited[i][j]) {
                    if (world[i][j].equals("Glitter") && !hasGold) {
                        System.out.print(" G ");
                    } else {
                        System.out.print(" . ");
                    }
                } else {
                    System.out.print(" * ");
                }
            }
            System.out.println();
        }
    }

    static void senseEnvironment() {
        String perception = world[x][y];
        visited[x][y] = true;
        System.out.println("Current Location (" + x + "," + y + ")");
        switch (perception) {
            case "Safe":
                System.out.println("Perception: It's safe here.");
                break;
            case "Breeze":
                System.out.println("Perception: You feel a breeze... A pit is nearby!");
                break;
            case "Wumpus":
                System.out.println("Perception: You smell a terrible stench... Wumpus is here!");
                break;
            case "Glitter":
                System.out.println("Perception: You see a glitter... GOLD is here!");
                break;
            case "Pit":
                System.out.println("Perception: You fell into a pit!");
                isAlive = false;
                break;
        }
    }

    static void move(int dx, int dy) {
        int nx = x + dx;
        int ny = y + dy;
        if (nx >= 0 && nx < 4 && ny >= 0 && ny < 4) {
            x = nx;
            y = ny;
            visited[x][y] = true;
            System.out.println("✅ Moved to (" + x + "," + y + ")");
            if (world[x][y].equals("Wumpus")) {
                System.out.println("💀 You were eaten by the Wumpus!");
                isAlive = false;
            } else if (world[x][y].equals("Pit")) {
                System.out.println("💀 You fell into a pit!");
                isAlive = false;
            }
        } else {
            System.out.println("❌ Invalid move! You hit a wall.");
        }
    }

    static void grabGold() {
        if (world[x][y].equals("Glitter")) {
            System.out.println("You grabbed the GOLD! Return to (0,0) to win.");
            hasGold = true;
            world[x][y] = "Safe";
        } else {
            System.out.println("There's no gold here!");
        }
    }

    static boolean checkWin() {
        return hasGold && x == 0 && y == 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Wumpus World Simulation!");
        System.out.println("Goal: Find the gold and return to (0,0). Avoid pits and the Wumpus!");

        visited[x][y] = true;

        while (isAlive) {
            if (checkWin()) {
                System.out.println("You returned with the gold! YOU WIN!");
                break;
            }

            printWorldView();
            displayMenu();

            int choice = scanner.nextInt();

            switch (choice) {
                case 1: move(-1, 0); break;
                case 2: move(1, 0); break;
                case 3: move(0, -1); break;
                case 4: move(0, 1); break;
                case 5: senseEnvironment(); break;
                case 6: grabGold(); break;
                case 7: System.out.println("Exiting Game. Goodbye!"); return;
                default: System.out.println("Invalid choice!"); break;
            }
        }

        if (!isAlive) {
            System.out.println("☠️ Game Over. You died!");
        }

        scanner.close();
    }
}
