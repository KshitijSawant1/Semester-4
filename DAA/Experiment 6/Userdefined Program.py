class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List to store edges

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
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u

        # Step 3: Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains a negative weight cycle")
                return None, None

        return dist, prev

    def print_shortest_paths(self, source):
        """Function to display shortest paths"""
        distances, predecessors = self.bellman_ford(source)

        # If negative cycle is detected, return
        if distances is None:
            return

        print(f"\nShortest distances from source vertex '{source}':")
        for vertex in range(self.V):
            path = []
            current = vertex
            while current is not None:
                path.append(str(current))
                current = predecessors[current]
            path.reverse()
            print(f"{source} → {vertex}: {distances[vertex]}, Path: {' → '.join(path)}")


# User Input for Custom Graph
def user_defined_graph():
    num_vertices = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))

    g = Graph(num_vertices)

    print("\nEnter the edges in the format (start_vertex end_vertex weight):")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        g.add_edge(u, v, weight)

    source = int(input("\nEnter the source vertex: "))
    
    # Run Bellman-Ford and display results
    g.print_shortest_paths(source)


# Run the User-Defined Graph Input
user_defined_graph()
