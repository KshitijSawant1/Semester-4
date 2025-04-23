### 🔍 Code Breakdown:

```python
def fcfs(requests, head):
```

- **Defines the function** `fcfs` that takes:
  - `requests`: a list of disk track numbers (requested positions on disk).
  - `head`: the current starting position of the disk head.

---

```python
    seek = 0
    sequence = []
```

- `seek`: a variable to **track total seek time** (the sum of all movements of the disk head).
- `sequence`: a list to **record the order** in which the requests are serviced.

---

```python
    for r in requests:
```

- Iterates over **each request** `r` in the `requests` list.

---

```python
        distance = abs(head - r)
```

- Calculates the **distance (seek time)** between the current `head` and the requested track `r`.
- `abs()` ensures it's always a positive value (absolute difference).

---

```python
        seek += distance
```

- **Accumulates the total seek time** by adding the distance just calculated.

---

```python
        sequence.append(r)
```

- Adds the request `r` to the `sequence` list to **record the seek path**.

---

```python
        head = r
```

- Updates the head position to the current request `r` to **simulate head movement**.

---

```python
    print("\n--- FCFS Disk Scheduling ---")
```

- Prints a section header for clarity.

---

```python
    print("Seek Sequence:", ' -> '.join(map(str, sequence)))
```

- Displays the full **seek sequence** in the order the requests were serviced, joined with `->`.

---

```python
    print("Total Seek Time:", seek)
```

- Displays the **total number of head movements** required to service all requests.

---

### 🧪 Example Execution:

```python
fcfs([82, 170, 43, 140, 24, 16, 190], head=50)
```

- The head starts at **50**, and services the requests in the **exact order** listed:
  1. From 50 to 82
  2. From 82 to 170
  3. 170 to 43, etc...

This models the **real-world scenario** where requests are handled in order of arrival (like a queue).

---
