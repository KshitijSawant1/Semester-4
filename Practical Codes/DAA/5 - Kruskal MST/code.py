class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False


def kruskal_mst(vertices, edges):
    mst = []
    dsu = DisjointSet(vertices)
    edges.sort(key=lambda edge: edge[2])  # Sort by weight

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))

    return mst


# ---------- Main Program ----------
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4),
    ('C', 'E', 2),
    ('D', 'E', 5)
]

mst_result = kruskal_mst(vertices, edges)

print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst_result:
    print(f"{u} -- {v} == {weight}")
