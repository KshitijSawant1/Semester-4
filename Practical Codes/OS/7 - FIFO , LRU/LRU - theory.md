### 🔹 Function Definition:

```python
def lru(pages, capacity):
```
- Defines a function `lru()` with two arguments:
  - `pages`: A list of page requests.
  - `capacity`: The number of slots available in memory (frames).

---

### 🔹 Initialization:

```python
    memory = []
    page_faults = 0
    page_hits = 0
```
- `memory`: Simulates the current state of memory (list of pages).
- `page_faults`: Counter for the number of page faults (misses).
- `page_hits`: Counter for the number of page hits (page already in memory).

---

### 🔹 Main Loop over Page Requests:

```python
    for page in pages:
```
- Iterates over each page request from the `pages` list.

---

### ✅ Page Hit Condition:

```python
        if page in memory:
            page_hits += 1
            # Move recently used page to the end
            memory.remove(page)
            memory.append(page)
```

- If the page is **already in memory**:
  - ✅ It's a **Page Hit** → increment `page_hits`.
  - Move the page to the **end of the list** to mark it as most recently used.
    - This simulates recent usage to help identify LRU pages for future faults.

---

### ❌ Page Fault Condition:

```python
        else:
            page_faults += 1
```
- If the page is **not in memory**, it's a **Page Fault** → increment `page_faults`.

---

### 🔄 Add or Replace Pages:

```python
            if len(memory) < capacity:
                memory.append(page)
```
- If memory is **not full**, simply add the page.

```python
            else:
                memory.pop(0)  # Remove least recently used
                memory.append(page)
```
- If memory **is full**, remove the **first (least recently used)** page in the list, then append the new one.

---

### 🖨️ Display Current State:

```python
        print(f"Page: {page} | Memory: {memory}")
```
- Prints the current page and the state of memory after the operation.

---

### 🔢 Calculate Ratios:

```python
    total_requests = len(pages)
    fault_ratio = page_faults / total_requests
    hit_ratio = page_hits / total_requests
```

- `total_requests`: Total number of page accesses.
- `fault_ratio`: Fraction of requests that caused page faults.
- `hit_ratio`: Fraction of requests that were page hits.

---

### 📊 Display Summary:

```python
    print("\nSummary:")
    print(f"Total Page Requests: {total_requests}")
    print(f"Total Page Faults  : {page_faults}")
    print(f"Total Page Hits    : {page_hits}")
    print(f"Page Fault Ratio   : {fault_ratio:.2f}")
    print(f"Page Hit Ratio     : {hit_ratio:.2f}")
```

- Displays final statistics for the simulation.

---

### ▶️ Example Input:

```python
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3
lru(pages, capacity)
```

- Simulates page replacement using LRU for the given page sequence and memory capacity.

---

### 🧠 Summary of Logic:
- LRU keeps the most recently used pages at the end of the `memory` list.
- Least Recently Used page is the **first element**.
- On each hit, move page to the end.
- On each fault:
  - If full → pop the front (LRU) and add new page.
  - If not full → append.

---
