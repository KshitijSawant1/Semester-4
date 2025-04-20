def sstf_disk_scheduling(requests, head):
    requests = requests.copy()
    total_seek = 0
    sequence = []
    print("\nOrder of service:")
    while requests:
        distances = [abs(head - track) for track in requests]
        min_index = distances.index(min(distances))
        closest = requests[min_index]
        distance = abs(head - closest)
        print(f"Head moved from {head} to {closest} [Seek: {distance}]")
        total_seek += distance
        head = closest
        sequence.append(closest)
        requests.pop(min_index)
    print(f"\nTotal Seek Time: {total_seek}")
    print(f"Average Seek Time: {total_seek / len(sequence):.2f}")

def menu_sstf():
    print("\n--- SSTF Disk Scheduling ---")
    print("1. Run with Default Input")
    print("2. Enter Custom Input")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice: ")
        if choice == '1':
            requests = [98, 183, 37, 122, 14, 124, 65, 67]
            head = 53
            print(f"\nDefault Request Queue: {requests}")
            print(f"Initial Head Position: {head}")
            sstf_disk_scheduling(requests, head)
        elif choice == '2':
            requests = list(map(int, input("Enter request queue (space separated): ").split()))
            head = int(input("Enter initial head position: "))
            sstf_disk_scheduling(requests, head)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

menu_sstf()
