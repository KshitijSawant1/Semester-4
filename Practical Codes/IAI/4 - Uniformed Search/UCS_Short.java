import java.util.*;

public class UCS_Short {
    static Map<Integer, List<int[]>> graph = new HashMap<>();

    static void addEdge(int u, int v, int cost) {
        graph.computeIfAbsent(u, k -> new ArrayList<>()).add(new int[]{v, cost});
        graph.computeIfAbsent(v, k -> new ArrayList<>()).add(new int[]{u, cost});
    }

    static void uniformCostSearch(int start, int goal) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        Map<Integer, Integer> dist = new HashMap<>();
        Map<Integer, Integer> parent = new HashMap<>();

        pq.offer(new int[]{start, 0});
        dist.put(start, 0);

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int u = node[0], cost = node[1];

            if (u == goal) {
                System.out.println("Goal: " + goal + ", Cost: " + cost);
                printPath(parent, goal);
                return;
            }

            for (int[] edge : graph.getOrDefault(u, new ArrayList<>())) {
                int v = edge[0], newCost = cost + edge[1];
                if (!dist.containsKey(v) || newCost < dist.get(v)) {
                    dist.put(v, newCost);
                    parent.put(v, u);
                    pq.offer(new int[]{v, newCost});
                }
            }
        }
        System.out.println("Goal not reachable.");
    }

    static void printPath(Map<Integer, Integer> parent, int node) {
        if (parent.containsKey(node)) printPath(parent, parent.get(node));
        System.out.print(node + " ");
    }

    public static void main(String[] args) {
        addEdge(0, 1, 2);
        addEdge(0, 2, 4);
        addEdge(1, 3, 7);
        addEdge(2, 3, 1);
        addEdge(3, 4, 3);

        Scanner sc = new Scanner(System.in);
        System.out.print("Start Node: ");
        int start = sc.nextInt();
        System.out.print("Goal Node: ");
        int goal = sc.nextInt();
        uniformCostSearch(start, goal);
        sc.close();
    }
}
