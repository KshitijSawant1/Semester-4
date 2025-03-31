Here is the **complete Python implementation** of **Experiment 04** for **CPU Scheduling Algorithms**: Round Robin (RR) and Shortest Job First (SJF), as per your provided theory and learning objectives.

---

## ✅ **Experiment 04: CPU Scheduling Algorithms – RR & SJF**

### 🧠 **Learning Objective:**
- Understand the working of Round Robin (RR) and Shortest Job First (SJF) scheduling.
- Observe and analyze CPU time sharing and scheduling efficiency.

---

## ⚙️ Menu-Driven Python Program

```python
def round_robin(processes, burst_time, quantum):
    n = len(processes)
    remaining_bt = burst_time[:]
    t = 0
    wt = [0] * n
    tat = [0] * n

    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                if remaining_bt[i] > quantum:
                    t += quantum
                    remaining_bt[i] -= quantum
                else:
                    t += remaining_bt[i]
                    wt[i] = t - burst_time[i]
                    remaining_bt[i] = 0
        if done:
            break

    for i in range(n):
        tat[i] = burst_time[i] + wt[i]

    print("\n--- Round Robin Scheduling ---")
    print("Process | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f"P{processes[i]}\t|\t{burst_time[i]}\t|\t{wt[i]}\t|\t{tat[i]}")
    print(f"\nAverage Waiting Time = {sum(wt)/n:.2f}")
    print(f"Average Turnaround Time = {sum(tat)/n:.2f}")


def sjf(processes, burst_time):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n

    combined = list(zip(processes, burst_time))
    combined.sort(key=lambda x: x[1])
    sorted_processes, sorted_bt = zip(*combined)

    for i in range(1, n):
        wt[i] = wt[i - 1] + sorted_bt[i - 1]

    for i in range(n):
        tat[i] = sorted_bt[i] + wt[i]

    print("\n--- Shortest Job First (SJF) Scheduling ---")
    print("Process | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f"P{sorted_processes[i]}\t|\t{sorted_bt[i]}\t|\t{wt[i]}\t|\t{tat[i]}")
    print(f"\nAverage Waiting Time = {sum(wt)/n:.2f}")
    print(f"Average Turnaround Time = {sum(tat)/n:.2f}")


def main_menu():
    while True:
        print("\n=== CPU Scheduling Menu ===")
        print("1. Round Robin Scheduling")
        print("2. Shortest Job First (SJF) Scheduling")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n-- Round Robin Scheduling --")
            default = input("Use default data? (y/n): ").lower()
            if default == 'y':
                processes = [1, 2, 3]
                burst_time = [24, 3, 3]
                quantum = 4
            else:
                n = int(input("Enter number of processes: "))
                processes = [i + 1 for i in range(n)]
                burst_time = list(map(int, input("Enter burst times: ").split()))
                quantum = int(input("Enter time quantum: "))
            round_robin(processes, burst_time, quantum)

        elif choice == '2':
            print("\n-- Shortest Job First Scheduling --")
            default = input("Use default data? (y/n): ").lower()
            if default == 'y':
                processes = [1, 2, 3]
                burst_time = [6, 8, 7]
            else:
                n = int(input("Enter number of processes: "))
                processes = [i + 1 for i in range(n)]
                burst_time = list(map(int, input("Enter burst times: ").split()))
            sjf(processes, burst_time)

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


# Run the menu
main_menu()
```

---

### 🧪 Default Examples:

- **RR Default Input:**
  - Processes: P1, P2, P3
  - Burst Times: [24, 3, 3]
  - Quantum: 4

- **SJF Default Input:**
  - Processes: P1, P2, P3
  - Burst Times: [6, 8, 7]

---

### 📘 Result & Discussion:
- Round Robin ensures fairness using time quantum.
- SJF minimizes average waiting time by executing shortest tasks first.
- Both algorithms have their use cases:
  - RR: time-sharing systems
  - SJF: batch systems

---

### 🎯 Learning Outcomes:
- LO1: Ability to Understand the working of the Round Robin scheduling algorithm.
- LO2: Ability to implement SJF scheduling and its focus on minimizing waiting time.

---

### 🏁 Course Outcomes:
- CO: Apply and compare CPU scheduling techniques and measure system performance.

---

Let me know if you need:
- Gantt chart for visualization 🧾  
- Preemptive version of SJF ⏳  
- Report writing or conclusion section ✍️  
- Output screenshot simulation 💻