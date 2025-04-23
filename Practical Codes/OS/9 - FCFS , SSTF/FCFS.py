def fcfs(requests, head):
    seek = 0
    sequence = []

    for r in requests:
        distance = abs(head - r)
        seek += distance
        sequence.append(r)
        head = r

    print("\n--- FCFS Disk Scheduling ---")
    print("Seek Sequence:", ' -> '.join(map(str, sequence)))
    print("Total Seek Time:", seek)

# 🔹 Example
fcfs([82, 170, 43, 140, 24, 16, 190], head=50)
