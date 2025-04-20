def scan_disk_scheduling(requests, head, direction):
    seek_sequence = []
    total_seek = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    left.sort()
    right.sort()

    if direction == "left":
        for track in reversed(left):
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track
        for track in right:
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track
    else:
        for track in right:
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track
        for track in reversed(left):
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track

    return seek_sequence, total_seek


def look_disk_scheduling(requests, head, direction):
    seek_sequence = []
    total_seek = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    left.sort()
    right.sort()

    if direction == "left":
        for track in reversed(left):
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track
        for track in right:
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track
    else:
        for track in right:
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track
        for track in reversed(left):
            seek_sequence.append(track)
            total_seek += abs(head - track)
            head = track

    return seek_sequence, total_seek


def main():
    default_requests = [98, 183, 37, 122, 14, 124, 65, 67]
    default_head = 53
    default_direction = "right"

    while True:
        print("\n========== Disk Scheduling Algorithms ==========")
        print("1. SCAN with Default Input")
        print("2. SCAN with Custom Input")
        print("3. LOOK with Default Input")
        print("4. LOOK with Custom Input")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            seek_sequence, total_seek = scan_disk_scheduling(default_requests, default_head, default_direction)
            print("\nSCAN (Default Input):")
            print("Requests:", default_requests)
            print("Seek Sequence:", seek_sequence)
            print("Total Seek Count:", total_seek)

        elif choice == '2':
            n = int(input("Enter number of requests: "))
            requests = list(map(int, input("Enter the disk requests: ").split()))
            head = int(input("Enter initial head position: "))
            direction = input("Enter direction (left/right): ").lower()
            seek_sequence, total_seek = scan_disk_scheduling(requests, head, direction)
            print("\nSCAN (Custom Input):")
            print("Seek Sequence:", seek_sequence)
            print("Total Seek Count:", total_seek)

        elif choice == '3':
            seek_sequence, total_seek = look_disk_scheduling(default_requests, default_head, default_direction)
            print("\nLOOK (Default Input):")
            print("Requests:", default_requests)
            print("Seek Sequence:", seek_sequence)
            print("Total Seek Count:", total_seek)

        elif choice == '4':
            n = int(input("Enter number of requests: "))
            requests = list(map(int, input("Enter the disk requests: ").split()))
            head = int(input("Enter initial head position: "))
            direction = input("Enter direction (left/right): ").lower()
            seek_sequence, total_seek = look_disk_scheduling(requests, head, direction)
            print("\nLOOK (Custom Input):")
            print("Seek Sequence:", seek_sequence)
            print("Total Seek Count:", total_seek)

        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


main()
