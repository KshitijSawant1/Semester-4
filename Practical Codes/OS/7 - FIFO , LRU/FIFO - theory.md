---

### 🔍 Code Explanation:

```python
def fifo(pages, capacity):
```
- **Function Name:** `fifo`
- **Inputs:**
  - `pages`: list of page requests, e.g. `[1, 2, 3, 4, 1, 2, 5...]`
  - `capacity`: number of page frames available in memory.

---

```python
    memory = []
    page_faults = 0
    page_hits = 0
```
- `memory`: simulates the current content of RAM/page frames.
- `page_faults`: counts how many times a page had to be loaded (wasn't already in memory).
- `page_hits`: counts how many times a requested page was already in memory (no need to load again).

---

```python
    for page in pages:
```
- This loop runs through each page in the list `pages`.

---

```python
        if page in memory:
            page_hits += 1
```
- ✅ **Page Hit:** If the page is already in memory, it's a hit. Increase the `page_hits` counter.

---

```python
        else:
            page_faults += 1
```
- ❌ **Page Fault:** Page is not in memory. Increase the `page_faults`.

---

```python
            if len(memory) < capacity:
                memory.append(page)
```
- If there’s still space in memory (less than `capacity`), just add the page.

---

```python
            else:
                memory.pop(0)
                memory.append(page)
```
- If memory is full:
  - Remove the **oldest page** (`pop(0)`) — that’s FIFO!
  - Add the new page at the end.

---

```python
        print(f"Page: {page} | Memory: {memory}")
```
- After every request, print the current page and the memory state.

---

```python
    total_requests = len(pages)
    fault_ratio = page_faults / total_requests
    hit_ratio = page_hits / total_requests
```
- Calculate total page requests and ratios:
  - `fault_ratio`: how many times a page was **not found**.
  - `hit_ratio`: how many times a page **was already present**.

---

```python
    print("\nSummary:")
    print(f"Total Page Requests: {total_requests}")
    print(f"Total Page Faults  : {page_faults}")
    print(f"Total Page Hits    : {page_hits}")
    print(f"Page Fault Ratio   : {fault_ratio:.2f}")
    print(f"Page Hit Ratio     : {hit_ratio:.2f}")
```
- Display the final summary.

---

### 📌 Example Execution:
Given:
```python
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacity = 3
```

- FIFO will load pages into memory one by one.
- Once memory is full, it removes the oldest (first-in) page whenever a fault occurs.

---