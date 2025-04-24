def scan(requests, head, direction, disk_size):
    requests.append(head)
    requests.sort()
    seek = 0
    order = []

    head_index = requests.index(head)

    if direction == "right":
        right = requests[head_index:]
        left = requests[:head_index][::-1]
        seq = right + [disk_size - 1] + left
    else:
        left = requests[:head_index + 1][::-1]
        right = requests[head_index + 1:]
        seq = left + [0] + right

    for r in seq:
        if r != head:
            seek += abs(head - r)
            order.append(r)
            head = r

    print("\n--- SCAN Disk Scheduling ---")
    print("Seek Sequence:", ' -> '.join(map(str, order)))
    print("Total Seek Time:", seek)


req = [19,28,37,46,55,64,73,82,91]
head = 50 
direction = "right"
DS = 100
scan(req,head,direction,DS)