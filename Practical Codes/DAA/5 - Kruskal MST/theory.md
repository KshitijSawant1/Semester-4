## 🧱 CLASS: Disjoint Set Union (Union-Find)
```python
class DisjointSet:
```
Defines a class `DisjointSet`, which implements **Union-Find** — a data structure used to:
- Track **connected components**
- Efficiently **check and merge sets**

---

```python
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
```
- Constructor that initializes each node as **its own parent**.
- `self.parent` is a dictionary that helps identify the **set leader (root)** of each vertex.
- Initially, each vertex is in its own set.

---

```python
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
```
- `find()` function returns the **root/leader** of the set that `v` belongs to.
- Uses **path compression**: it makes the tree flat by pointing all nodes directly to the root for faster access in the future.

---

```python
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False
```
- `union()` merges the sets of `u` and `v` if they’re in **different sets**.
- Returns `True` if a merge happened (i.e., no cycle).
- Returns `False` if both are in the same set already (i.e., adding would create a **cycle**).

---

## 🚧 FUNCTION: Kruskal's MST
```python
def kruskal_mst(vertices, edges):
```
Defines the main function to compute the **Minimum Spanning Tree** using Kruskal's algorithm.

---

```python
    mst = []
```
An empty list to store the **edges in the final MST**.

---

```python
    dsu = DisjointSet(vertices)
```
Creates a **Disjoint Set Union (DSU)** object using the list of vertices.

---

```python
    edges.sort(key=lambda edge: edge[2])
```
Sorts the edges in **ascending order of weights**, because Kruskal's algorithm always picks the **smallest edge** first.

---

```python
    for u, v, weight in edges:
```
Iterates through each edge `(u, v, weight)` in the sorted list.

---

```python
        if dsu.union(u, v):
            mst.append((u, v, weight))
```
- Tries to join `u` and `v`.
- If they are in different components (no cycle), `union()` returns `True`, and the edge is added to the `mst`.

---

```python
    return mst
```
Returns the final list of MST edges.

---

## ▶️ MAIN PROGRAM

```python
vertices = ['A', 'B', 'C', 'D', 'E']
```
A list of graph vertices.

---

```python
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4),
    ('C', 'E', 2),
    ('D', 'E', 5)
]
```
- List of **edges in the graph**, where each edge is a tuple: `(node1, node2, weight)`
- The graph is **undirected**.

---

```python
mst_result = kruskal_mst(vertices, edges)
```
Calls the function `kruskal_mst()` and stores the resulting MST edges in `mst_result`.

---

```python
print("Edges in the Minimum Spanning Tree:")
```
Prints a header for the output.

---

```python
for u, v, weight in mst_result:
    print(f"{u} -- {v} == {weight}")
```
Prints each edge in the MST and its weight.

---

## 🧾 Sample Output
```
Edges in the Minimum Spanning Tree:
A -- B == 1
B -- C == 1
C -- E == 2
C -- D == 4
```

---

## 🔑 Key Concepts:
- **Kruskal’s Algorithm** is a **greedy** algorithm: always picks the smallest-weight edge that doesn't form a cycle.
- **Disjoint Set Union (Union-Find)** helps track whether adding an edge would form a cycle.
- The final MST connects all vertices with the **minimum total edge weight** and **no cycles**.
---

### ✅ **Kruskal’s Algorithm Analysis Table**

| **Aspect**        | **Complexity**             | **Reason / Explanation**                                                                                   |
|------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------|
| **Best Case**     | **O(E log E)**              | When the graph is already connected with minimal edge processing. Sorting dominates; few unions are done.   |
| **Average Case**  | **O(E log E)**              | Sorting of edges dominates, and Union-Find handles near-linear edge connection efficiently.                |
| **Worst Case**    | **O(E log E)**              | All edges are considered, and Union-Find still handles efficiently using path compression and union by rank.|
| **Space Complexity** | **O(V + E)**          | Stores: sorted edge list (E), parent array (V), rank array (V), and MST result (up to V−1 edges).           |

---

### 🔍 Explanation:

#### 🔹 Time Complexity:

- **Sorting Edges** takes `O(E log E)` — this is always done regardless of graph connectivity.
- **Union-Find operations** for each edge are nearly **O(1)** on average (amortized) with **path compression + union by rank**.
- So overall time is **dominated by edge sorting**: **O(E log E)** in all cases.

> **Note:** Since `E` can be up to `V²`, the worst-case time becomes `O(E log V²)` = `O(E log V)` using the fact that `log E ≈ log V² = 2 log V`.

#### 🔹 Space Complexity:

- **O(E)** for storing and sorting edges
- **O(V)** for:
  - `parent[]` array (Disjoint Set)
  - `rank[]` array (for efficient union)
  - `MST[]` result storage

So, total is **O(V + E)**.

---

### ✅ **Kruskal’s vs Prim’s Algorithm – Detailed Comparison**

| **Criteria**                 | **Kruskal’s Algorithm**                       | **Prim’s Algorithm**                                 |
|-----------------------------|-----------------------------------------------|-------------------------------------------------------|
| **Approach**                | Greedy; picks the **smallest edge** that doesn’t form a cycle | Greedy; grows the MST from a **starting vertex**       |
| **Data Structures Used**    | Disjoint Set (Union-Find)                     | Min-Heap / Priority Queue, Adjacency List or Matrix   |
| **Graph Representation**    | Works better with **Edge List**               | Works better with **Adjacency List or Matrix**        |
| **Time Complexity**         | O(E log E)                                    | O(E + V log V) with Min-Heap and Adjacency List       |
| **Space Complexity**        | O(V + E)                                      | O(V + E)                                               |
| **Best For**                | **Sparse graphs**                             | **Dense graphs**                                      |
| **Cycle Detection**         | Yes, uses **Union-Find** to detect cycles     | No need; edges chosen from already visited nodes      |
| **Edge Selection Strategy** | Global – considers all edges                  | Local – always chooses the closest node to MST        |
| **Starting Node Required?** | **No**                                        | **Yes** – needs a starting vertex                     |
| **MST Output**              | May be disconnected if graph is disconnected  | Always connected if the graph is connected            |

---

### 🧠 Quick Takeaways:

- **Kruskal's** is better when:
  - You already have an **edge list**
  - The graph is **sparse**
  - You want to understand **cycle detection via Union-Find**

- **Prim's** is better when:
  - You work with **dense graphs**
  - You already have **adjacency list/matrix**
  - You want to **grow the MST node by node**

---