def look(requests, head, direction):
    requests.sort()
    seek = 0
    order = []

    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    seq = right + left[::-1] if direction == "right" else left[::-1] + right

    for r in seq:
        seek += abs(head - r)
        order.append(r)
        head = r

    print("Sequence:", ' -> '.join(map(str, order)))
    print("Total Seek Operations:", seek)

# 🔹 Example
look([82, 170, 43, 140, 24, 16, 190], head=50, direction="right")
