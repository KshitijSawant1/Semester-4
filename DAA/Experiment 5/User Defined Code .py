# User-defined Disjoint Set (Union-Find) Data Structure
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}

    def find(self, vertex):
        """Find the root of the set where the vertex belongs."""
        if self.parent[vertex] == vertex:
            return vertex
        self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        """Union two sets that contain vertex1 and vertex2."""
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            self.parent[root2] = root1  # Attach one root to another


# Kruskal's Algorithm with User Input
def kruskal(graph, vertices):
    mst = []  # List to store MST edges
    total_weight = 0  # Store total weight of MST

    # Step 1: Sort edges based on weight (ascending order)
    graph.sort(key=lambda edge: edge[2])

    # Step 2: Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)

    # Step 3: Process edges in ascending order
    for edge in graph:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)
            total_weight += weight

    # Step 4: Display the MST
    print("\nEdges in the Minimum Spanning Tree (MST):")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")
    print("Total Weight of MST:", total_weight)


# Menu-Driven Program
def menu():
    vertices = []
    graph = []

    while True:
        print("\nKruskal's Algorithm Menu")
        print("1. Enter vertices")
        print("2. Enter edges")
        print("3. Find MST using Kruskal's Algorithm")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            vertices = input("Enter the vertices (separated by spaces): ").split()
            print(f"Vertices: {vertices}")

        elif choice == 2:
            if not vertices:
                print("Please enter vertices first (Option 1).")
                continue

            u = input("Enter starting vertex: ")
            v = input("Enter ending vertex: ")
            weight = int(input("Enter the weight of the edge: "))
            if u in vertices and v in vertices:
                graph.append((u, v, weight))
                print("Edge added successfully.")
            else:
                print("Invalid vertices. Please enter valid vertex names.")

        elif choice == 3:
            if not graph:
                print("Please enter at least one edge before running the algorithm.")
                continue
            kruskal(graph, vertices)

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the Menu
menu()
