def rr(at, bt, q):
    n = len(at)
    rt = bt[:]
    t = 0
    wt = [0]*n
    tat = [0]*n
    done = [0]*n

    while sum(done) < n:
        for i in range(n):
            if at[i] <= t and rt[i] > 0:
                use = min(q, rt[i])
                t += use
                rt[i] -= use
                if rt[i] == 0:
                    tat[i] = t - at[i]
                    wt[i] = tat[i] - bt[i]
                    done[i] = 1

    total_wt = sum(wt)
    total_tat = sum(tat)
    
    print("Process\tAT\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1} \t {at[i]} \t {bt[i]} \t {wt[i]} \t {tat[i]}")
    
    print(f"\nTotal WT = {total_wt}, Average WT = {total_wt/n}")
    print(f"Total TAT = {total_tat}, Average TAT = {total_tat/n}")


# rr([0, 1, 2], [5, 3, 6], 2)
rr([0, 1, 2,3], [3, 1, 5,4], 2)
