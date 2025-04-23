def sjf(at, bt):
    n = len(at)
    processes = list(range(n))
    completed = [False]*n
    t = 0
    wt, tat, st = [0]*n, [0]*n, [0]*n

    while not all(completed):
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if at[i] <= t and not completed[i] and bt[i] < min_bt:
                min_bt = bt[i]
                idx = i
        if idx == -1:
            t += 1
            continue
        st[idx] = t
        wt[idx] = t - at[idx]
        t += bt[idx]
        tat[idx] = t - at[idx]
        completed[idx] = True
    total_wt = sum(wt)
    total_tat = sum(tat)
    
    print("Process\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1} \t {at[i]} \t {bt[i]} \t {wt[i]} \t {tat[i]}")
    
    print(f"\nTotal WT = {total_wt}, Average WT = {total_wt/n:.2f}")
    print(f"Total TAT = {total_tat}, Average TAT = {total_tat/n:.2f}")

# Example usage
sjf([0, 2, 4, 6], [8, 4, 2, 1])
