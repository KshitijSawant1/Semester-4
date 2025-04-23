### 🧠 Function Definition
```python
def rr(at, bt, q):
```
- `rr` is the function name.
- `at`: list of **arrival times** for each process.
- `bt`: list of **burst times** for each process.
- `q`: the **time quantum** (fixed CPU time slice per process).

---

### 🧠 Initialization
```python
    n = len(at)                # Number of processes
    rt = bt[:]                 # Remaining time for each process (copy of burst time)
    t = 0                      # Current time (simulation clock)
    wt = [0]*n                 # Waiting Time array initialized to 0
    tat = [0]*n                # Turnaround Time array initialized to 0
    done = [0]*n               # Done flag for each process (0 = not finished, 1 = finished)
```

---

### 🔁 Loop Until All Processes Are Done
```python
    while sum(done) < n:
```
- `sum(done)` gives the count of completed processes.
- Continue looping until all processes are marked `done`.

---

### 🧮 Check Each Process
```python
        for i in range(n):
```
- Loop through each process index `i`.

---

### ✅ If Process Has Arrived and Has Time Left
```python
            if at[i] <= t and rt[i] > 0:
```
- `at[i] <= t`: process has **arrived** by current time `t`.
- `rt[i] > 0`: it still has some **remaining burst time**.

---

### 🔄 Allocate Minimum of Time Quantum or Remaining Time
```python
                use = min(q, rt[i])
```
- Take the **minimum** of time quantum `q` and the remaining time `rt[i]`.

---

### ⏳ Simulate Execution
```python
                t += use
                rt[i] -= use
```
- Advance the **simulation clock** `t` by `use` units.
- Reduce the **remaining burst time** accordingly.

---

### 🎯 If Process is Finished
```python
                if rt[i] == 0:
                    tat[i] = t - at[i]                # Turnaround Time = Completion Time - Arrival Time
                    wt[i] = tat[i] - bt[i]            # Waiting Time = Turnaround - Burst
                    done[i] = 1                       # Mark process as completed
```
- Calculate **Turnaround Time** and **Waiting Time**.
- Set `done[i]` to 1 (finished).

---

### 📊 After Completion of All
```python
    total_wt = sum(wt)
    total_tat = sum(tat)
```
- Sum all **Waiting Times** and **Turnaround Times**.

---

### 📋 Print Results
```python
    print("Process\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1} \t {at[i]} \t {bt[i]} \t {wt[i]} \t {tat[i]}")
```
- Display a formatted table:
  - **AT**: Arrival Time  
  - **BT**: Burst Time  
  - **WT**: Waiting Time  
  - **TAT**: Turnaround Time

---

### 📈 Show Totals and Averages
```python
    print(f"\nTotal WT = {total_wt}, Average WT = {total_wt/n:.2f}")
    print(f"Total TAT = {total_tat}, Average TAT = {total_tat/n:.2f}")
```
- Show:
  - Total and Average Waiting Time
  - Total and Average Turnaround Time

---

### ✅ Example Call:
```python
rr([0, 1, 2, 3], [3, 1, 5, 4], 2)
```
- 4 Processes
- Arrival Times: 0, 1, 2, 3
- Burst Times: 3, 1, 5, 4
- Time Quantum = 2

---