def calculate_need(need, maxm, allot, n, m):
    for i in range(n):
        for j in range(m):
            need[i][j] = maxm[i][j] - allot[i][j]

def is_safe(n, m, avail, maxm, allot):
    need = [[0] * m for _ in range(n)]
    calculate_need(need, maxm, allot, n, m)

    finish = [False] * n
    safe_seq = []
    work = avail[:]

    while len(safe_seq) < n:
        allocated = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allot[i][j]
                    safe_seq.append(i)
                    finish[i] = True
                    allocated = True
        if not allocated:
            break

    if len(safe_seq) == n:
        print("\nSystem is in a SAFE state.")
        print("Safe Sequence:", ' -> '.join(f"P{p}" for p in safe_seq))
    else:
        print("\n❌ System is in an UNSAFE state.")

def default_data():
    n = 5  # Processes
    m = 3  # Resources
    allot = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    maxm = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    avail = [3, 3, 2]
    return n, m, avail, maxm, allot

def custom_input():
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resource types: "))

    print("\nEnter Allocation Matrix:")
    allot = [[int(x) for x in input(f"P{i}: ").split()] for i in range(n)]

    print("\nEnter Maximum Matrix:")
    maxm = [[int(x) for x in input(f"P{i}: ").split()] for i in range(n)]

    print("\nEnter Available Resources:")
    avail = [int(x) for x in input().split()]
    return n, m, avail, maxm, allot

def main():
    while True:
        print("\n==== Banker's Algorithm Menu ====")
        print("1. Run with Default Example")
        print("2. Enter Custom Input")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\nRunning Default Banker’s Algorithm Example...")
            n, m, avail, maxm, allot = default_data()
            is_safe(n, m, avail, maxm, allot)
        elif choice == '2':
            print("\nEnter Custom Input for Banker’s Algorithm...")
            n, m, avail, maxm, allot = custom_input()
            is_safe(n, m, avail, maxm, allot)
        elif choice == '3':
            print("Exiting Program. Thank you!")
            break
        else:
            print("Invalid choice! Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
