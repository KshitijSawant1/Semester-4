def fcfs_disk_scheduling(requests, head):
    total_seek = 0
    print("\nOrder of service:")
    for track in requests:
        distance = abs(head - track)
        print(f"Head moved from {head} to {track} [Seek: {distance}]")
        total_seek += distance
        head = track
    print(f"\nTotal Seek Time: {total_seek}")
    print(f"Average Seek Time: {total_seek / len(requests):.2f}")

def menu_fcfs():
    print("\n--- FCFS Disk Scheduling ---")
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
            fcfs_disk_scheduling(requests, head)
        elif choice == '2':
            requests = list(map(int, input("Enter request queue (space separated): ").split()))
            head = int(input("Enter initial head position: "))
            fcfs_disk_scheduling(requests, head)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

menu_fcfs()
