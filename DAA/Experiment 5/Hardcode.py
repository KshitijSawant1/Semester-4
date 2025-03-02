class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])  # Path compression
            return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root2] = root1

def kruskal(graph):
    mst = []
    edges = sorted(graph, key=lambda item: item[2])  # Sort by weight
    vertices = set()
    for u, v, _ in graph:
        vertices.add(u)
        vertices.add(v)

    disjoint_set = DisjointSet(vertices)

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)

    return mst

# Example graph: (u, v, weight)
graph = [
    ('A', 'B', 4),
    ('A', 'H', 8),
    ('B', 'C', 8),
    ('B', 'H', 11),
    ('C', 'D', 7),
    ('C', 'F', 4),
    ('C', 'I', 2),
    ('D', 'E', 9),
    ('D', 'F', 14),
    ('E', 'F', 10),
    ('F', 'G', 2),
    ('G', 'H', 1),
    ('G', 'I', 6),
    ('H', 'I', 7),
]

# Running Kruskal's algorithm
mst = kruskal(graph)
print("Edges in the Minimum Spanning Tree:")
total_weight = 0
for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")
    total_weight += weight

print("Total Weight of MST:", total_weight)
