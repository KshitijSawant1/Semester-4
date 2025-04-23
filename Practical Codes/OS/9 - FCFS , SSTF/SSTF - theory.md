### ✅ Code Breakdown:

```python
def sstf(requests, head):
```
- **Function Definition**: Defines a function `sstf` which takes:
  - `requests`: A list of disk track numbers to be serviced.
  - `head`: The current position of the disk head.

---

```python
    sequence = []
    seek = 0
    visited = [False] * len(requests)
```
- `sequence`: Stores the order in which disk requests are processed.
- `seek`: Accumulates the total seek time (distance head moves).
- `visited`: A boolean list to track which requests have already been serviced.

---

```python
    for _ in range(len(requests)):
```
- Runs the scheduling for **as many times as there are requests**.

---

```python
        min_distance = float('inf')
        index = -1
```
- Initializes variables to **track the nearest request**:
  - `min_distance` is set to infinity (will be reduced).
  - `index` will store the index of the closest unvisited request.

---

```python
        for i, req in enumerate(requests):
            if not visited[i]:
                distance = abs(head - req)
                if distance < min_distance:
                    min_distance = distance
                    index = i
```
- Loops through each request:
  - If it's **not yet visited**, calculate distance from the current head.
  - Keeps track of the **closest unvisited request** (`min_distance` and `index`).

---

```python
        seek += min_distance
        head = requests[index]
        sequence.append(head)
        visited[index] = True
```
- After finding the **closest request**:
  - `seek` is increased by the distance moved.
  - `head` is updated to new position.
  - The request is added to the **final seek sequence**.
  - It is marked as **visited**.

---

```python
    print("\n--- SSTF Disk Scheduling ---")
    print("Seek Sequence:", ' -> '.join(map(str, sequence)))
    print("Total Seek Time:", seek)
```
- Final Output:
  - Shows the **order** in which requests were handled.
  - Displays **total seek time** 

---

### 🔹 Example Used:
```python
sstf([82, 170, 43, 140, 24, 16, 190], head=50)
```
- Disk requests = `[82, 170, 43, 140, 24, 16, 190]`
- Head starts at `50`

This example will calculate the most optimal nearest request (based on absolute distance from head) at every step until all requests are completed.

---
