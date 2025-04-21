Absolutely! Here's a **line-by-line breakdown** of your **Uniform Cost Search (UCS)** Java program. I'll explain each line clearly and concisely:

---

### 🔹 `import java.util.*;`

- Imports all classes from the `java.util` package.
- Includes classes like `Scanner`, `Map`, `HashMap`, `List`, `ArrayList`, `PriorityQueue`, etc.

---

### 🔹 `public class UCS_Short {`

- Declares the class named `UCS_Short`.

---

### 🔹 `static Map<Integer, List<int[]>> graph = new HashMap<>();`

- Declares a static **graph** as an adjacency list.
- Each node (`Integer`) maps to a list of its neighbors.
- Each neighbor is stored as an `int[]` array: `{neighbor, cost}`.

---

## 🧩 addEdge Method

### 🔹 `static void addEdge(int u, int v, int cost) {`

- Method to add an undirected edge between `u` and `v` with the given `cost`.

### 🔹 `graph.computeIfAbsent(u, k -> new ArrayList<>()).add(new int[]{v, cost});`

- If node `u` is not already in the graph, adds it with an empty list.
- Then adds `{v, cost}` to `u`'s adjacency list.

### 🔹 `graph.computeIfAbsent(v, k -> new ArrayList<>()).add(new int[]{u, cost});`

- Similarly, adds `{u, cost}` to `v`'s adjacency list.
- Since the graph is undirected, both directions are stored.

---

## 🔍 uniformCostSearch Method

### 🔹 `static void uniformCostSearch(int start, int goal) {`

- This method performs UCS from `start` node to `goal` node.

### 🔹 `PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));`

- Creates a **priority queue** to store nodes as `{node, cost}`.
- Orders the queue by `cost` (ascending) to always pick the lowest cost node.

### 🔹 `Map<Integer, Integer> dist = new HashMap<>();`

- `dist` keeps track of the **shortest distance found so far** to each node.

### 🔹 `Map<Integer, Integer> parent = new HashMap<>();`

- `parent` stores the **previous node** for each visited node (used for printing the path).

---

### 🔹 `pq.offer(new int[]{start, 0});`

- Adds the start node to the queue with cost 0.

### 🔹 `dist.put(start, 0);`

- Initializes the start node's cost to 0 in the distance map.

---

### 🔹 `while (!pq.isEmpty()) {`

- Main UCS loop: keep running until there are nodes in the queue.

---

### 🔹 `int[] node = pq.poll();`

- Retrieves and removes the node with **lowest cost** from the queue.

### 🔹 `int u = node[0], cost = node[1];`

- Extracts the `node` and its `cost`.

---

### 🔹 `if (u == goal) {`

- If the goal node is reached, print result and path.

### 🔹 `System.out.println("Goal: " + goal + ", Cost: " + cost);`

- Displays the total cost to reach the goal.

### 🔹 `printPath(parent, goal);`

- Calls helper function to print the actual path taken.

### 🔹 `return;`

- Exits the search loop.

---

### 🔹 `for (int[] edge : graph.getOrDefault(u, new ArrayList<>())) {`

- Loops over all neighbors of current node `u`.

### 🔹 `int v = edge[0], newCost = cost + edge[1];`

- Extracts neighbor `v` and calculates the **new total cost** to reach `v`.

---

### 🔹 `if (!dist.containsKey(v) || newCost < dist.get(v)) {`

- If node `v` is unvisited **or** a cheaper path is found:

### 🔹 `dist.put(v, newCost);`

- Update `v`'s shortest distance.

### 🔹 `parent.put(v, u);`

- Store `u` as parent of `v`.

### 🔹 `pq.offer(new int[]{v, newCost});`

- Add the neighbor with its new cost to the priority queue.

---

### 🔹 `System.out.println("Goal not reachable.");`

- If loop ends without finding the goal.

---

## 📦 printPath Method

### 🔹 `static void printPath(Map<Integer, Integer> parent, int node) {`

- Recursive function to print the **path from start to goal** using the `parent` map.

### 🔹 `if (parent.containsKey(node)) printPath(parent, parent.get(node));`

- If the current node has a parent, recursively print from parent first.

### 🔹 `System.out.print(node + " ");`

- Prints the current node (after all parents are printed first).

---

## 🧪 main Method

### 🔹 `public static void main(String[] args) {`

- The entry point of the program.

---

### 🔹 `addEdge(...)`

- Adds edges to define the graph (customizable).

---

### 🔹 `Scanner sc = new Scanner(System.in);`

- Creates a `Scanner` object to read user input.

---

### 🔹 `System.out.print("Start Node: "); int start = sc.nextInt();`

- Reads the **starting node** from the user.

### 🔹 `System.out.print("Goal Node: "); int goal = sc.nextInt();`

- Reads the **goal node** from the user.

---

### 🔹 `uniformCostSearch(start, goal);`

- Calls the UCS function to compute the optimal path and cost.

---

### 🔹 `sc.close();`

- Closes the input scanner.

---

## 🧠 Example Walkthrough

### Input:
```
Start Node: 3
Goal Node: 6
```

### Path:
- 3 → 5 → 7 → 6

### Output:
```
Goal: 6, Cost: 6
3 5 7 6
```

---

Would you like me to convert this into a **visual diagram** or help you trace it step-by-step with a sample graph?