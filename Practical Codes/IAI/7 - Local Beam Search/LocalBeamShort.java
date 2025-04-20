import java.util.*;

public class LocalBeamShort {

    static int evaluate(int x) {
        return -(x * x) + 10 * x;
    }

    static List<Integer> getNeighbors(int x) {
        List<Integer> n = new ArrayList<>();
        if (x > 0) n.add(x - 1);
        if (x < 20) n.add(x + 1);
        return n;
    }

    static void beamSearch(int k, int maxIter) {
        Random rand = new Random();
        List<Integer> states = new ArrayList<>();
        for (int i = 0; i < k; i++) states.add(rand.nextInt(21));

        for (int i = 0; i < maxIter; i++) {
            List<Integer> neighbors = new ArrayList<>();
            for (int s : states) neighbors.addAll(getNeighbors(s));
            neighbors.sort((a, b) -> evaluate(b) - evaluate(a));
            states = neighbors.subList(0, Math.min(k, neighbors.size()));
        }

        int best = states.get(0);
        System.out.println("Best x: " + best + ", f(x): " + evaluate(best));
    }

    public static void main(String[] args) {
        beamSearch(3, 10); // k = 3, max iterations = 10
    }
}
