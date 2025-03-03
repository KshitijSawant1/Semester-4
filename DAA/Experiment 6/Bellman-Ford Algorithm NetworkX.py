import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List to store graph edges

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
                return None, None

        return dist, prev

    def visualize_graph(self, source):
        """Visualize the graph before and after applying Bellman-Ford"""
        G = nx.DiGraph()
        
        # Add edges to NetworkX graph
        for u, v, weight in self.edges:
            G.add_edge(u, v, weight=weight)

        # Run Bellman-Ford Algorithm
        distances, predecessors = self.bellman_ford(source)

        # Check if the graph contains a negative cycle
        if distances is None:
            print("Cannot visualize as the graph contains a negative weight cycle.")
            return

        # Define layout for better visualization
        pos = nx.spring_layout(G)

        # Draw the original graph
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=12, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Original Graph")

        # Draw the shortest path tree
        shortest_path_edges = [(predecessors[v], v) for v in range(self.V) if predecessors[v] is not None]

        plt.subplot(1, 2, 2)
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, font_size=12, font_weight='bold')
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='red', width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color='red', node_size=1000)
        plt.title("Shortest Path Tree from Source")

        # Show the visualization
        plt.show()

        # Print shortest path distances
        print(f"\nShortest distances from source vertex '{source}':")
        for vertex in range(self.V):
            print(f"{source} → {vertex}: {distances[vertex]}")

# Create a graph with 5 vertices (0 to 4)
g = Graph(5)

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

# Define source vertex
source = 0

# Visualize the graph and shortest path
g.visualize_graph(source)
