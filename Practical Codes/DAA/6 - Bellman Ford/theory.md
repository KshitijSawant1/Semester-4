## ✅ Function: `bellman_ford(vertices, edges, start)`
```python
def bellman_ford(vertices, edges, start):
```
Defines the function that implements the **Bellman-Ford algorithm**.  
It takes:
- `vertices`: list of all nodes (e.g. `['A', 'B', 'C']`)
- `edges`: list of all edges in the form `(u, v, weight)`
- `start`: the source node to compute shortest paths from

---

### 🔹 Step 1: Initialize distances
```python
    distance = {v: float('inf') for v in vertices}
```
Creates a dictionary `distance` where each vertex initially has a distance of **infinity** (i.e., unreachable).

```python
    distance[start] = 0
```
The distance from the source node to itself is **0**.

---

### 🔹 Step 2: Relax all edges V-1 times
```python
    for _ in range(len(vertices) - 1):
```
We repeat the **edge relaxation process** exactly **(V - 1)** times, where `V` is the number of vertices.

```python
        for u, v, w in edges:
```
Loop over each edge from node `u` to node `v` with weight `w`.

```python
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
```
Check if:
1. `u` is reachable (i.e., its distance is not infinity)
2. The current known distance to `v` can be improved via `u`

```python
                distance[v] = distance[u] + w
```
Update `distance[v]` with the new **shorter** distance.

This is the **core of Bellman-Ford**: edge relaxation.

---

### 🔹 Step 3: Check for Negative Weight Cycles
```python
    for u, v, w in edges:
```
Loop through all edges again one more time.

```python
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
```
If you can still relax an edge **after V-1 iterations**, a **negative weight cycle exists**.

```python
            print("Graph contains a negative weight cycle")
            return None
```
Abort the algorithm and return `None`, because shortest paths are **not valid** due to the cycle.

---

### 🔹 Step 4: Return Final Distances
```python
    return distance
```
Return the dictionary of shortest distances from the start node to all others.

---

## ✅ Main Program

### 🔹 Define Vertices
```python
vertices = ['A', 'B', 'C', 'D', 'E']
```
List of all nodes in the graph.

---

### 🔹 Define Edges
```python
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 3),
    ('B', 'D', 2),
    ('B', 'E', 3),
    ('C', 'B', 1),
    ('C', 'D', 4),
    ('D', 'E', 2),
    ('E', 'D', 1)
]
```
- Each tuple `(u, v, w)` represents an **edge from `u` to `v`** with weight `w`.
- Note: there are **bidirectional paths** between some nodes (e.g., `D` and `E`), and all edge weights are positive (so no negative cycle).

---

### 🔹 Run the Algorithm
```python
start_node = 'A'
shortest_paths = bellman_ford(vertices, edges, start_node)
```
- Sets `'A'` as the source node
- Calls `bellman_ford()` to get the shortest distances

---

### 🔹 Print the Results
```python
if shortest_paths:
    print(f"Shortest distances from node '{start_node}':")
    for node in shortest_paths:
        print(f"{start_node} → {node} = {shortest_paths[node]}")
```
- If there's **no negative weight cycle**, print all shortest paths from `'A'`.
- Format: `A → B = 3`, `A → D = 5`, etc.

---

## ✅ Output:
Expected:
```
Shortest distances from node 'A':
A → A = 0
A → B = 3
A → C = 2
A → D = 5
A → E = 6
```

---

## 🔁 How This Worked:
- `A → C = 2`
- `C → B = 1` → total `A → B = 3`
- `C → D = 4` → total `A → D = 6`, but `B → D = 2` gives better: `A → B → D = 3 + 2 = 5`
- `D → E = 2` → total `A → D → E = 5 + 2 = 7`, but `B → E = 3` gives better: `A → B → E = 3 + 3 = 6`

---

### ✅ **Bellman-Ford Algorithm Analysis Table**

| **Aspect**         | **Complexity**       | **Reason / Explanation**                                                                                  |
|--------------------|----------------------|-------------------------------------------------------------------------------------------------------------|
| **Best Case**       | **O(E)**             | If all shortest distances are found in the **first iteration**, algorithm can stop early *(with optimization)*. |
| **Average Case**    | **O(V × E)**         | Standard case: relax all edges **(V−1) times**, typical in many graphs.                                     |
| **Worst Case**      | **O(V × E)**         | Even if no distances change, the algorithm **still performs V−1 full passes** over all edges.               |
| **Space Complexity**| **O(V)**             | Stores `distance[]` for each vertex. Optionally `predecessor[]` for path reconstruction.                    |

---

### 🔍 Explanation:

#### 🔹 Time Complexity:

- **Best Case (Optimized)**: If distances converge in 1 or 2 iterations, the algorithm can exit early. Time becomes linear in edges: **O(E)**.
  - Needs **extra logic** to break early (early exit flag).
  
- **Average/Worst Case**: The algorithm runs `V - 1` iterations (where V = number of vertices), relaxing **all E edges** each time.
  - Time = `(V - 1) × E` = **O(V × E)**

#### 🔹 Space Complexity:

- Stores:
  - `distance[]` → to hold shortest distance from source to each vertex → **O(V)**
  - `predecessor[]` (optional) → to reconstruct the shortest path → **O(V)**

No adjacency matrix or heap used — just linear storage.

---
### 🧠 When to Use Bellman-Ford:

- When the graph has **negative edge weights**.
- When you need to **detect negative weight cycles**.
- Not as efficient as Dijkstra's for positive-weight graphs.

---

### ✅ **Bellman-Ford vs Dijkstra – Comparison Table**

| **Aspect**                    | **Bellman-Ford Algorithm**                    | **Dijkstra’s Algorithm**                                |
|------------------------------|-----------------------------------------------|----------------------------------------------------------|
| **Approach**                 | Dynamic Programming                           | Greedy                                                   |
| **Edge Weights**             | Works with **positive and negative** weights  | Works only with **non-negative** weights                |
| **Negative Weight Cycles**   | **Can detect** negative cycles                | **Cannot detect** negative cycles                       |
| **Time Complexity (Adj List)**| **O(V × E)**                                   | **O((V + E) log V)** with min-heap & adjacency list     |
| **Space Complexity**         | O(V)                                          | O(V) with heap + O(E) for adjacency list                |
| **Shortest Path Updates**    | Repeats **V−1 edge relaxations**              | Uses **priority queue** to choose shortest known path    |
| **Early Termination**        | Possible (with optimization)                 | Implicit through greedy min extraction                  |
| **Path Reconstruction**      | Needs a predecessor array                     | Needs a predecessor array                               |
| **Graph Type Suitability**   | Works for **general graphs**                  | Works for **dense, non-negative-weighted graphs**       |
| **Algorithm Nature**         | **Slower** but more **versatile**             | **Faster** but **restricted** by weight constraints     |
| **Cycle Detection**          | Yes – reports negative cycle presence         | No – cannot handle cycles with negative total weight    |

---

### 🧠 Summary:

| **Use Bellman-Ford when...**                              | **Use Dijkstra when...**                               |
|-----------------------------------------------------------|--------------------------------------------------------|
| The graph has **negative edge weights**                   | All edge weights are **non-negative**                  |
| You want to **detect negative weight cycles**             | You want a **faster algorithm** for large dense graphs |
| You're okay with **O(V × E)** time for smaller graphs     | You want optimal performance with **min-heap + list**  |

---

### 🧾 Example Scenario:

- Graph with negative edge (e.g., time discounts or cashbacks):  
  ✅ Use **Bellman-Ford**

- GPS routing or latency-based network graphs with positive weights only:  
  ✅ Use **Dijkstra**

---