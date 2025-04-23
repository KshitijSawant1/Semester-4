---

### 🔍 **Code Explanation**

```python
def scan(requests, head, direction, disk_size):
```
- Defines the `scan` function.
- Parameters:
  - `requests`: list of disk track numbers requested by processes.
  - `head`: current position of the disk head.
  - `direction`: which direction the head moves ("right" or "left").
  - `disk_size`: total number of cylinders on the disk (like 0–199 for a 200-size disk).

---

```python
    requests.append(head)
    requests.sort()
```
- Add the current head position into the `requests` list to correctly position it in the seek sequence.
- Sort the list to process requests in ascending order.

---

```python
    seek = 0
    order = []
```
- `seek`: will hold total seek operations (total head movements).
- `order`: list to store the sequence in which tracks are accessed.

---

```python
    head_index = requests.index(head)
```
- Find the index of the head in the sorted list of requests.

---

### 🧭 Direction Handling
```python
    if direction == "right":
        right = requests[head_index:]
        left = requests[:head_index][::-1]
        seq = right + [disk_size - 1] + left
```
- If head is moving right:
  - `right`: all requests from current head to the end (inclusive).
  - `left`: all requests before head in reverse (to serve after hitting end).
  - `disk_size - 1`: simulates going all the way to the disk edge (like cylinder 199).
  - Final `seq` is rightward tracks + end + reversed left (like elevator going to the top and coming back).

```python
    else:
        left = requests[:head_index + 1][::-1]
        right = requests[head_index + 1:]
        seq = left + [0] + right
```
- If head is moving left:
  - `left`: from head to start (inclusive), reversed.
  - `right`: the tracks that will be served after bouncing at 0.
  - `0`: represents going to the lowest edge of disk.
  - Final `seq` is leftward tracks + 0 + rightward tracks.

---

### 🔁 Seek Calculation Loop

```python
    for r in seq:
        if r != head:
            seek += abs(head - r)
            order.append(r)
            head = r
```
- Loop through each track in the final sequence.
- Skip the current head position to avoid redundant calculation.
- `abs(head - r)`: distance moved by the disk arm.
- Add the seek to total.
- Append this track to the final access `order`.
- Update `head` to new position.

---

### 📄 Final Output

```python
    print("\n--- SCAN Disk Scheduling ---")
    print("Seek Sequence:", ' -> '.join(map(str, order)))
    print("Total Seek Time:", seek)
```
- Prints the final seek order and total movement done by the disk head.

---

### ✅ Example Call

```python
scan([82, 170, 43, 140, 24, 16, 190], head=50, direction="right", disk_size=200)
```
- Disk head starts at position `50`, moving towards the **right**.
- Processes the right-hand side requests first until end (199), then comes back left.

---