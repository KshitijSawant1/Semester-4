### 🔍 **Code:**

```python
def look(requests, head, direction):
```
- **Function definition**: `look` takes in:
  - `requests`: A list of track numbers requested by processes.
  - `head`: The current position of the disk head.
  - `direction`: The direction of head movement (`"right"` or `"left"`).

---

```python
    requests.sort()
```
- **Sorts the request list** so that the head can move in an orderly direction (from low to high or vice versa).
- Sorting makes it easier to go in one direction and then reverse.

---

```python
    seek = 0
    order = []
```
- `seek`: Keeps track of the total head movement (seek time).
- `order`: Stores the order in which the requests are serviced (the sequence of accesses).

---

```python
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
```
- Splits the requests into:
  - `left`: All tracks that are **less than** the head position.
  - `right`: All tracks that are **greater than or equal to** the head position.

---

```python
    seq = right + left[::-1] if direction == "right" else left[::-1] + right
```
- **Creates the actual service order (seq)**:
  - If `direction == "right"`: First go right (increasing), then reverse back left.
    - So `right + left[::-1]`
  - Else: Go left (decreasing), then reverse back right.
    - So `left[::-1] + right`
- `[::-1]` is used to **reverse** the list, because we are going toward lower track numbers.

---

```python
    for r in seq:
        seek += abs(head - r)
        order.append(r)
        head = r
```
- For every request `r` in the service sequence:
  - `abs(head - r)`: Calculate the distance (seek) between current head and the next track.
  - Add it to total `seek`.
  - Append the current request to `order` (for visualization).
  - Update `head` to the current position.

---

```python
    print("Sequence:", ' -> '.join(map(str, order)))
    print("Total Seek Operations:", seek)
```
- **Output**:
  - Print the full service order (seek sequence).
  - Show total seek operations (i.e., total head movements across all track requests).

---

### 🧪 **Example Output**
If you run:
```python
look([82, 170, 43, 140, 24, 16, 190], head=50, direction="right")
```

You'll get:
```
Sequence: 82 -> 140 -> 170 -> 190 -> 43 -> 24 -> 16
Total Seek Operations: 208
```

This means:
- Head first moves to 82, then to 140, 170, 190 (right direction).
- Then reverses and goes to 43, 24, 16 (left direction).
- Total distance moved by the head = 208 units.

---