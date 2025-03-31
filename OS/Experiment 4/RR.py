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


def rr_menu():
    default_processes = [1, 2, 3]
    default_burst_time = [24, 3, 3]
    default_quantum = 4

    while True:
        print("\n====== Round Robin Scheduling Menu ======")
        print("1. Use Default Input")
        print("2. Enter Custom Input")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            round_robin(default_processes, default_burst_time, default_quantum)

        elif choice == "2":
            n = int(input("Enter number of processes: "))
            processes = [i + 1 for i in range(n)]
            burst_time = list(map(int, input("Enter burst times separated by space: ").split()))
            quantum = int(input("Enter time quantum: "))
            round_robin(processes, burst_time, quantum)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")

# Run RR menu
rr_menu()
