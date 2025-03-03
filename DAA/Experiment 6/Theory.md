### **🚀 Experiment 5: Bellman-Ford Algorithm Using Dynamic Programming**

---

## **🎯 Learning Objective**
- To **find the Single Source Shortest Path (SSSP)** using the **Bellman-Ford Algorithm**.
- To analyze the algorithm’s performance and its ability to handle **negative weight edges**.

---

## **🛠️ Tools Required**
- Programming Languages: **C/C++/Java/Python**
- Platforms: **Windows** or **Linux**

---

## **📚 Theory**

### **What is the Bellman-Ford Algorithm?**
- **Bellman-Ford** is a **Dynamic Programming-based** algorithm used to find the **shortest paths** from a **single source vertex** to **all other vertices** in a weighted graph.
- Unlike **Dijkstra's Algorithm**, Bellman-Ford **works with negative weight edges**.
- If a **negative weight cycle** exists in the graph, the algorithm detects it.

---

### **🔍 Algorithm Steps (Dynamic Programming Approach)**

1. **Initialize**:
   - Set the **distance** of all vertices to **∞ (infinity)** except the **source vertex**, which is set to **0**.
   - Initialize a **predecessor array** to store the path.

2. **Relax all edges** **\(V - 1\) times**:
   - For each edge **(u, v, weight)**:
     - If **dist[u] + weight < dist[v]**, update **dist[v]** and **prev[v]**.

3. **Check for Negative Weight Cycles**:
   - If an edge still satisfies **dist[u] + weight < dist[v]**, then the graph contains a **negative weight cycle**.

---

### **📑 Algorithm (Pseudocode)**

```plaintext
function BellmanFord(Graph, Source):
    Initialize dist[] to ∞, except dist[Source] = 0
    Initialize prev[] to NULL

    For i from 1 to V-1:
        For each edge (u, v, weight) in Graph:
            If dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u

    For each edge (u, v, weight):
        If dist[u] + weight < dist[v]:
            Report "Negative Weight Cycle Exists"

    Return dist[], prev[]
```

---

## **💻 Python Code for Bellman-Ford Algorithm**

```python
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List to store graph edges

    def add_edge(self, u, v, weight):
        """Function to add edges to the graph"""
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        """Bellman-Ford Algorithm"""
        # Step 1: Initialize distances
        dist = {v: float('inf') for v in range(self.V)}
        prev = {v: None for v in range(self.V)}
        dist[source] = 0  # Distance to the source is 0

        # Step 2: Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u

        # Step 3: Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] + weight < dist[v]:
                print("Graph contains a negative weight cycle")
                return None

        return dist, prev

# Create Graph
g = Graph(5)  # 5 vertices (0 to 4)

# Add edges (u, v, weight)
g.add_edge(0, 1, 6)
g.add_edge(0, 2, 7)
g.add_edge(1, 2, 8)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, -4)
g.add_edge(2, 3, -3)
g.add_edge(2, 4, 9)
g.add_edge(3, 1, -2)
g.add_edge(4, 3, 7)

# Run Bellman-Ford Algorithm from source vertex 0
source = 0
distances, predecessors = g.bellman_ford(source)

# Display Results
if distances:
    print(f"\nShortest distances from source vertex '{source}':")
    for vertex in range(g.V):
        print(f"{source} → {vertex}: {distances[vertex]}")
```

---

## **🔍 Example Execution**

**Input Graph:**
```
        (6)
    0 --------> 1
    |          / | \
   (7)      (8) | (-4)
    |     /     |    \
    v  (-3)     |     v
    2 --------> 3 ----> 4
           (-2)      (7)
```

**Output:**
```
Shortest distances from source vertex '0':
0 → 0: 0
0 → 1: 6
0 → 2: 7
0 → 3: 4
0 → 4: 2
```

---

## **📊 Complexity Analysis**
| Step | Time Complexity |
|------|---------------|
| **Initialization** | \( O(V) \) |
| **Edge Relaxation (V-1 times)** | \( O(VE) \) |
| **Negative Cycle Detection** | \( O(E) \) |
| **Total Complexity** | **\( O(VE) \)** |

---

## **✅ Advantages of Bellman-Ford Algorithm**
1. **Works with negative weight edges**.
2. **Detects negative weight cycles**.
3. **Simpler than Dijkstra’s Algorithm**.

## **❌ Disadvantages**
1. **Slower than Dijkstra’s Algorithm** (\( O(VE) \) vs. \( O((V + E) \log V) \)).
2. **Not efficient for dense graphs**.

---

## **📌 Applications**
- **Routing in Networks** (Finding shortest paths in **computer networks**).
- **Detecting Arbitrage in Currency Exchange** (Finding **profitable currency trades**).
- **Distributed Systems** (**Message Passing Protocols**).
- **Railway and Flight Network Analysis**.

---

## **🎯 Learning Outcome**
- Students should be able to **understand and apply Bellman-Ford** for **Single Source Shortest Path (SSSP)** problems.
- Analyze the time complexity and understand its **use cases**.

## **📚 Course Outcome**
- Upon completion, students will be able to **apply dynamic programming** to solve real-world graph problems.

---

### **🔚 Conclusion**
- The **Bellman-Ford Algorithm** is a **dynamic programming approach** for the **SSSP problem**.
- It **handles negative weights**, unlike **Dijkstra’s Algorithm**.
- The algorithm runs in **\( O(VE) \) time**, making it **less efficient for dense graphs**.
- It is **widely used in network routing, currency exchange, and shortest path calculations**.

🚀 **Would you like a visualization of the Bellman-Ford Algorithm using `NetworkX`?**