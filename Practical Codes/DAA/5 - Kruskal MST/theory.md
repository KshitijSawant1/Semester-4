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
