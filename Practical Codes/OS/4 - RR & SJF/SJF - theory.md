### ✅ **Code Explanation (Line-by-Line)**

```python
def sjf(at, bt):
```
- This is the main function.
- `at` = list of Arrival Times.
- `bt` = list of Burst Times.

---

```python
    n = len(at)
```
- Number of processes.
  
```python
    done = [0]*n
```
- Keeps track of whether each process has completed (`0 = not done`, `1 = done`).

```python
    t = 0
```
- The current time in the simulation (CPU clock).

```python
    wt, tat, st = [0]*n, [0]*n, [0]*n
```
- `wt` = Waiting Time  
- `tat` = Turnaround Time  
- `st` = Start Time for each process

---

```python
    while sum(done)<n:
```
- Loop until all processes are completed.

```python
        idx = -1
        min_bt = float('inf')
```
- `idx`: to store the index of the next process to schedule.
- `min_bt`: stores the shortest burst time among ready (arrived) processes.

```python
        for i in range(n):
            if at[i] <= t and not done[i] and bt[i] < min_bt:
                min_bt = bt[i]
                idx = i
```
- Finds the next process with the **shortest burst time** that has **already arrived** and is **not yet completed**.

```python
        if idx == -1:
            t += 1
            continue
```
- If no process is ready at current time `t`, increment time and check again.

---

### ✅ If a process is selected

```python
        st[idx] = t
```
- Records the **start time** of the process.

```python
        wt[idx] = st[idx] - at[idx]
```
- Calculates **waiting time**:  
  Start Time − Arrival Time

```python
        t += bt[idx]
```
- Move time forward by that process's burst time.

```python
        tat[idx] = t - at[idx]
```
- Turnaround Time = Finish Time − Arrival Time

```python
        done[idx] = 1
```
- Mark this process as completed.

---

### ✅ Summary and Output

```python
    total_wt = sum(wt)
    total_tat = sum(tat)
```
- Total waiting time and total turnaround time (for average).

```python
    print("Process\tAT\tBT\tST\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1} \t {at[i]} \t {bt[i]} \t {st[i]} \t {wt[i]} \t {tat[i]}")
```
- Prints per-process details in tabular format:
  - Arrival Time, Burst Time, Start Time, Waiting Time, Turnaround Time.

```python
    print(f"\nTotal WT = {total_wt}, Average WT = {total_wt/n}")
    print(f"Total TAT = {total_tat}, Average TAT = {total_tat/n}")
```
- Final summary: total and average waiting/turnaround time.

---

### 🧪 Example Usage:

```python
sjf([0, 2, 4, 6], [8, 4, 2, 1])
```

- Four processes:
  - P1: AT=0, BT=8
  - P2: AT=2, BT=4
  - P3: AT=4, BT=2
  - P4: AT=6, BT=1

The CPU picks shortest jobs first *among arrived ones*.

---
