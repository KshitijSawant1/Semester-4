def banker(allocated, maximum, available):
    num_processes = len(allocated)
    num_resources = len(available)

    # Calculate 'need' = max - allocated
    need = []
    for i in range(num_processes):
        need.append([maximum[i][j] - allocated[i][j] for j in range(num_resources)])

    finish = [False] * num_processes
    sequence = []

    while True:
        found = False
        for i in range(num_processes):
            if not finish[i]:
                if all(need[i][j] <= available[j] for j in range(num_resources)):
                    # Simulate resource allocation
                    for j in range(num_resources):
                        available[j] += allocated[i][j]
                    finish[i] = True
                    sequence.append(f"P{i}")
                    found = True
        if not found:
            break

    if all(finish):
        print("System is in a Safe State.")
        print("Safe Sequence:", " -> ".join(sequence))
    else:
        print("System is NOT in a Safe State.")

# 🔹 Example Input
allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
maximum   = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
available = [3, 3, 2]

banker(allocated, maximum, available)
