import java.util.*;

public class LocalBeamSearch {

    // Objective function: f(x) = -x^2 + 10x
    static int evaluate(int x) {
        return -(x * x) + 10 * x;
    }

    // Generate neighbors: here simply +1 and -1 steps
    static List<Integer> getNeighbors(int x) {
        List<Integer> neighbors = new ArrayList<>();
        if (x > 0) neighbors.add(x - 1);
        if (x < 20) neighbors.add(x + 1); // Range limit
        return neighbors;
    }

    // Local Beam Search
    static int localBeamSearch(int k, int maxIterations) {
        Random rand = new Random();

        // Step 1: Generate k random initial states
        List<Integer> currentStates = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            currentStates.add(rand.nextInt(21)); // random from 0 to 20
        }

        int bestValue = Integer.MIN_VALUE;
        int bestState = -1;

        for (int iter = 0; iter < maxIterations; iter++) {
            List<Integer> allNeighbors = new ArrayList<>();
            for (int state : currentStates) {
                allNeighbors.addAll(getNeighbors(state));
            }

            // Sort neighbors by objective function
            allNeighbors.sort((a, b) -> Integer.compare(evaluate(b), evaluate(a)));

            // Keep top k
            currentStates.clear();
            for (int i = 0; i < k && i < allNeighbors.size(); i++) {
                currentStates.add(allNeighbors.get(i));
            }

            // Track the best solution
            int currentBest = currentStates.get(0);
            int currentValue = evaluate(currentBest);
            if (currentValue > bestValue) {
                bestValue = currentValue;
                bestState = currentBest;
            }
        }

        System.out.println("Best x: " + bestState);
        System.out.println("Best f(x): " + bestValue);
        return bestState;
    }

    // Menu
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\n===== Local Beam Search Menu =====");
            System.out.println("1. Run Local Beam Search");
            System.out.println("2. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter beam width (k): ");
                    int k = scanner.nextInt();
                    System.out.print("Enter max iterations: ");
                    int maxIterations = scanner.nextInt();
                    localBeamSearch(k, maxIterations);
                    break;
                case 2:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice! Try again.");
            }
        } while (choice != 2);
    }
}
