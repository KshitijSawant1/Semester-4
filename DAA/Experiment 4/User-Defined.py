import heapq

# Dijkstra's Algorithm Implementation
def dijkstra(graph, source):
    # Step 1: Initialize distance dictionary
    dist = {vertex: float('infinity') for vertex in graph}
    dist[source] = 0  # Distance to the source is 0

    # Step 2: Use priority queue (min-heap) for optimization
    priority_queue = [(0, source)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the popped vertex has a higher distance, skip
        if current_distance > dist[current_vertex]:
            continue

        # Step 3: Update distances of neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist


# Menu-Driven User-Defined Graph Input
def menu():
    graph = {}

    while True:
        print("\nDijkstra’s Algorithm Menu")
        print("1. Add vertex")
        print("2. Add edge")
        print("3. Find shortest paths from source")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            vertex = input("Enter vertex name: ")
            if vertex not in graph:
                graph[vertex] = {}
                print(f"Vertex '{vertex}' added.")
            else:
                print("Vertex already exists.")

        elif choice == 2:
            u = input("Enter the start vertex: ")
            v = input("Enter the end vertex: ")
            weight = int(input("Enter the weight of the edge: "))
            if u in graph and v in graph:
                graph[u][v] = weight
                graph[v][u] = weight  # Assuming an undirected graph
                print(f"Edge added between '{u}' and '{v}' with weight {weight}.")
            else:
                print("One or both vertices not found!")

        elif choice == 3:
            if not graph:
                print("Graph is empty. Please add vertices and edges first.")
                continue
            source = input("Enter the source vertex: ")
            if source not in graph:
                print("Source vertex not found.")
                continue

            distances = dijkstra(graph, source)
            print(f"\nShortest distances from source vertex '{source}':")
            for vertex in distances:
                print(f"{source} → {vertex}: {distances[vertex]}")

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")


# Run Menu
menu()
