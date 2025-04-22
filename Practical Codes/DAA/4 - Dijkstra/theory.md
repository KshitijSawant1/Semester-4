---

### 🔹 Importing Required Module

```python
import heapq
```

- This imports the `heapq` module, which allows us to use a **priority queue (min-heap)**.
- It ensures we always process the **node with the current smallest distance** efficiently.

---

### 🔹 Dijkstra Function Definition

```python
def dijkstra(graph, start):
```

- This defines the `dijkstra` function.
- Parameters:
  - `graph`: a dictionary representing an adjacency list
  - `start`: the node from where we calculate shortest paths

---

### 🔹 Distance Initialization

```python
    distances = {node: float('inf') for node in graph}
```

- Initializes a `distances` dictionary to store shortest distances from the `start` node to every other node.
- Initially, all distances are set to `infinity` (i.e., unknown or unreachable).

```python
    distances[start] = 0
```

- The distance to the starting node from itself is always 0.

---

### 🔹 Priority Queue Setup

```python
    priority_queue = [(0, start)]
```

- Initializes a min-heap (priority queue) with a single entry: `(0, start)`.
- Format: `(distance, node)`
- It ensures that the node with the **smallest tentative distance** is processed first.

---

### 🔹 Main Loop: Explore All Nodes

```python
    while priority_queue:
```

- This loop runs until the priority queue is empty.
- It keeps processing nodes in order of shortest distance found so far.

---

### 🔹 Get Node with Smallest Distance

```python
        current_distance, current_node = heapq.heappop(priority_queue)
```

- Pops the node with the **smallest distance** from the priority queue.

---

### 🔹 Skip If Already Processed Better Path

```python
        if current_distance > distances[current_node]:
            continue
```

- If we already found a **shorter path** to this node before, we skip processing it again.
- This avoids unnecessary work.

---

### 🔹 Traverse Neighbors

```python
        for neighbor, weight in graph[current_node]:
```

- Iterates over all **adjacent nodes (neighbors)** of the current node.
- Each neighbor is connected with an edge having a certain `weight`.

---

### 🔹 Calculate Distance Through Current Node

```python
            distance = current_distance + weight
```

- Calculates the **total distance** from `start` → `current_node` → `neighbor`.

---

### 🔹 Update Distance If Shorter Path Found

```python
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
```

- If this new path is **shorter** than the previously recorded distance:
  - Update the `distances` dictionary
  - Add the neighbor into the priority queue with the **updated distance**

---

### 🔹 Return the Final Distances

```python
    return distances
```

- Once all reachable nodes are processed, return the dictionary containing **shortest distances** from the `start` node.

---

### 🔹 Graph Definition (Adjacency List)

```python
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}
```

- A dictionary where:
  - Keys are node names
  - Values are lists of `(neighbor, weight)` tuples

#### Graph Visual:

```
A --4--> B
A --1--> C
C --2--> B
C --5--> D
B --1--> D
```

---

### 🔹 Set Starting Node

```python
start_node = 'A'
```

- The algorithm will find the shortest paths from node `'A'`.

---

### 🔹 Call the Algorithm

```python
shortest_paths = dijkstra(graph, start_node)
```

- Calls the `dijkstra` function with the `graph` and `start_node`
- Stores the result in `shortest_paths`, which will be a dictionary

---

### 🔹 Print the Results

```python
print(f"Shortest distances from node '{start_node}':")
for node in shortest_paths:
    print(f"{start_node} → {node} = {shortest_paths[node]}")
```

- Iterates through the `shortest_paths` dictionary
- Prints the shortest distance from the `start_node` to each node in the graph

---

### 🧾 Example Output

```
Shortest distances from node 'A':
A → A = 0
A → B = 3
A → C = 1
A → D = 4
```

---
