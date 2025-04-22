def bellman_ford(vertices, edges, start):
    distance = {v: float('inf') for v in vertices}
    distance[start] = 0

    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distance


vertices = ['A', 'B', 'C', 'D', 'E']
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

start_node = 'A'
shortest_paths = bellman_ford(vertices, edges, start_node)

if shortest_paths:
    print(f"Shortest distances from node '{start_node}':")
    for node in shortest_paths:
        print(f"{start_node} → {node} = {shortest_paths[node]}")
