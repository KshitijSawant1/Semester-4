import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Dijkstra's Algorithm Implementation
def dijkstra(graph, source):
    dist = {vertex: float('infinity') for vertex in graph}
    dist[source] = 0  # Distance to the source is 0

    priority_queue = [(0, source)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if we've already found a better path
        if current_distance > dist[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist


# Hardcoded Graph (Adjacency List Representation)
graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'A': 4, 'C': 8, 'H': 11},
    'C': {'B': 8, 'D': 7, 'F': 4, 'I': 2},
    'D': {'C': 7, 'E': 9, 'F': 14},
    'E': {'D': 9, 'F': 10},
    'F': {'C': 4, 'D': 14, 'E': 10, 'G': 2},
    'G': {'F': 2, 'H': 1, 'I': 6},
    'H': {'A': 8, 'B': 11, 'G': 1, 'I': 7},
    'I': {'C': 2, 'G': 6, 'H': 7}
}

# Define the source vertex
source = 'A'

# Run Dijkstra’s Algorithm
distances = dijkstra(graph, source)

# Display the shortest distances
print(f"\nShortest distances from source vertex '{source}':")
for vertex in distances:
    print(f"{source} → {vertex}: {distances[vertex]}")

# Visualizing the Graph using NetworkX
G = nx.Graph()

# Add edges to the NetworkX graph
for u in graph:
    for v, weight in graph[u].items():
        G.add_edge(u, v, weight=weight)

# Draw the graph
pos = nx.spring_layout(G)  # Layout for better visualization
plt.figure(figsize=(10, 6))
nx.draw(
    G, pos, with_labels=True, node_color='lightblue',
    node_size=800, font_size=12, font_weight='bold'
)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Highlight the shortest paths from the source
shortest_paths = [(source, v) for v in distances if v != source]
nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color='red')
plt.title("Graph Representation with Dijkstra's Shortest Paths")
plt.show()
