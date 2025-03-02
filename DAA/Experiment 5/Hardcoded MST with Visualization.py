import networkx as nx
import matplotlib.pyplot as plt

# Define a hardcoded graph
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
    ('H', 'I', 7)
]

# Initialize a NetworkX graph
G = nx.Graph()

# Add edges to the graph
for u, v, weight in graph:
    G.add_edge(u, v, weight=weight)


# Kruskal's Algorithm to find MST
def kruskal(graph):
    mst = []
    sorted_edges = sorted(graph, key=lambda edge: edge[2])  # Sort by weight
    parent = {}

    # Disjoint Set helper functions
    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(vertex1, vertex2):
        root1 = find(vertex1)
        root2 = find(vertex2)
        parent[root1] = root2

    # Initialize disjoint sets
    for u, v, _ in graph:
        parent[u] = u
        parent[v] = v

    # Process edges
    for u, v, weight in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))

    return mst


# Generate MST using Kruskal's Algorithm
mst_edges = kruskal(graph)

# Visualize the Original Graph
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos = nx.spring_layout(G)  # Position the nodes using a force-directed layout
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=12)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Original Graph")

# Visualize the Minimum Spanning Tree (MST)
plt.subplot(1, 2, 2)
MST = nx.Graph()
for u, v, weight in mst_edges:
    MST.add_edge(u, v, weight=weight)

nx.draw(MST, pos, with_labels=True, node_color='lightgreen', node_size=800, font_size=12)
mst_labels = {(u, v): weight for u, v, weight in mst_edges}
nx.draw_networkx_edge_labels(MST, pos, edge_labels=mst_labels)
plt.title("Minimum Spanning Tree (MST)")

# Show the plot
plt.show()

# Print MST Edges and Total Weight
total_weight = sum([weight for _, _, weight in mst_edges])
print("Edges in MST:")
for u, v, weight in mst_edges:
    print(f"{u} - {v}: {weight}")
print("Total Weight of MST:", total_weight)
