```python
def sjf(at, bt):
```
🧠 **Defines a function `sjf`** that takes:
- `at`: a list of **arrival times** for each process.
- `bt`: a list of **burst times** (how long each process needs on CPU).

---

```python
    n = len(at)
```
🧮 **Calculates the number of processes** (`n`) based on how many arrival times are given.

---

```python
    processes = list(range(n))
```
🧾 **Creates a list of process indices**, like `[0, 1, 2, ..., n-1]`, to keep track of process IDs.

---

```python
    completed = [False]*n
```
✅ A list to **track which processes are completed**. Initially, all set to `False`.

---

```python
    t = 0
```
⏲️ `t` is the **current system time**. It keeps increasing as processes execute.

---

```python
    wt, tat, st = [0]*n, [0]*n, [0]*n
```
📊 Initialize:
- `wt`: Waiting Time
- `tat`: Turnaround Time
- `st`: Start Time  
All initialized to 0 for every process.

---

```python
    while not all(completed):
```
🔁 **Main loop**: Runs **until all processes are marked as completed**.

---

```python
        idx = -1
        min_bt = float('inf')
```
📍 Temporary variables:
- `idx`: will store the **index of the selected process**.
- `min_bt`: to store the **smallest burst time found**.

---

```python
        for i in range(n):
            if at[i] <= t and not completed[i] and bt[i] < min_bt:
                min_bt = bt[i]
                idx = i
```
🔍 **Finds the next process to execute**:
- Must have **already arrived** (`at[i] <= t`).
- Must be **not completed**.
- Must have the **smallest burst time** among eligible ones.

---

```python
        if idx == -1:
            t += 1
            continue
```
⌛ If **no process has arrived** yet (`idx == -1`), just **wait** by incrementing `t` and **retry**.

---

```python
        st[idx] = t
```
🕓 **Start Time** of selected process is the current time.

---

```python
        wt[idx] = t - at[idx]
```
🧾 **Waiting Time** is: Start Time – Arrival Time.

---

```python
        t += bt[idx]
```
🚀 Advance the time by the **burst time** of the process (it runs to completion).

---

```python
        tat[idx] = t - at[idx]
```
📈 **Turnaround Time** is: Completion Time – Arrival Time.

---

```python
        completed[idx] = True
```
✅ Mark the selected process as **completed**.

---

```python
    total_wt = sum(wt)
    total_tat = sum(tat)
```
📊 Compute **total waiting time** and **total turnaround time**.

---

```python
    print("Process\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1} \t {at[i]} \t {bt[i]} \t {wt[i]} \t {tat[i]}")
```
🖨️ Print a table of:
- Process ID
- Arrival Time
- Burst Time
- Waiting Time
- Turnaround Time

---

```python
    print(f"\nTotal WT = {total_wt}, Average WT = {total_wt/n:.2f}")
    print(f"Total TAT = {total_tat}, Average TAT = {total_tat/n:.2f}")
```
📉 Display **total** and **average** Waiting Time and Turnaround Time.

---

### 📌 Example Input
```python
sjf([0, 2, 4, 6], [8, 4, 2, 1])
```

This means:
- `P1`: arrives at 0, needs 8 units
- `P2`: arrives at 2, needs 4 units
- `P3`: arrives at 4, needs 2 units
- `P4`: arrives at 6, needs 1 unit

They’ll be picked **based on shortest burst time** *among the arrived processes*.

---