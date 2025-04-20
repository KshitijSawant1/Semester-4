import java.util.*;

public class AStarShort {

    static class Node implements Comparable<Node> {
        int id, g, h;
        Node(int id, int g, int h) { this.id = id; this.g = g; this.h = h; }
        public int compareTo(Node o) { return Integer.compare(g + h, o.g + o.h); }
    }

    static Map<Integer, List<int[]>> graph = new HashMap<>();
    static Map<Integer, Integer> heuristic = new HashMap<>();

    static void addEdge(int u, int v, int cost) {
        graph.computeIfAbsent(u, k -> new ArrayList<>()).add(new int[]{v, cost});
    }

    static void aStar(int start, int goal) {
        PriorityQueue<Node> open = new PriorityQueue<>();
        Map<Integer, Integer> dist = new HashMap<>(), parent = new HashMap<>();
        open.add(new Node(start, 0, heuristic.get(start))); dist.put(start, 0);

        while (!open.isEmpty()) {
            Node curr = open.poll();
            if (curr.id == goal) {
                printPath(parent, goal); return;
            }
            for (int[] edge : graph.getOrDefault(curr.id, List.of())) {
                int next = edge[0], cost = curr.g + edge[1];
                if (!dist.containsKey(next) || cost < dist.get(next)) {
                    dist.put(next, cost); parent.put(next, curr.id);
                    open.add(new Node(next, cost, heuristic.get(next)));
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
        addEdge(0,1,2); addEdge(0,2,4); addEdge(1,3,7);
        addEdge(2,3,1); addEdge(3,4,3);
        heuristic.put(0,7); heuristic.put(1,6); heuristic.put(2,2);
        heuristic.put(3,1); heuristic.put(4,0); // Goal

        aStar(0, 4); // Start=0, Goal=4
    }
}
