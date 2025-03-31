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


def sjf_menu():
    default_processes = [1, 2, 3]
    default_burst_time = [6, 8, 7]

    while True:
        print("\n====== Shortest Job First (SJF) Scheduling Menu ======")
        print("1. Use Default Input")
        print("2. Enter Custom Input")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sjf(default_processes, default_burst_time)

        elif choice == "2":
            n = int(input("Enter number of processes: "))
            processes = [i + 1 for i in range(n)]
            burst_time = list(map(int, input("Enter burst times separated by space: ").split()))
            sjf(processes, burst_time)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")

# Run SJF menu
sjf_menu()
