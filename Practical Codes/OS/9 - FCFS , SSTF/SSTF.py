def sstf(requests, head):
    sequence = []
    seek = 0
    visited = [False] * len(requests)

    for _ in range(len(requests)):
        min_distance = float('inf')
        index = -1
        for i, req in enumerate(requests):
            if not visited[i]:
                distance = abs(head - req)
                if distance < min_distance:
                    min_distance = distance
                    index = i
        # Update seek and head
        seek += min_distance
        head = requests[index]
        sequence.append(head)
        visited[index] = True

    print("\n--- SSTF Disk Scheduling ---")
    print("Seek Sequence:", ' -> '.join(map(str, sequence)))
    print("Total Seek Time:", seek)
  
req = [19,28,37,46,55,64,73,82,91]
head = 50 
sstf(req,head)