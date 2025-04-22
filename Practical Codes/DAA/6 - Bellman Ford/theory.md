---

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