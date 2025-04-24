def sjf(at, bt):
    n = len(at)
    done = [0]*n
    t = 0
    wt, tat, st = [0]*n, [0]*n, [0]*n

    while sum(done)<n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if at[i] <= t and not done[i] and bt[i] < min_bt:
                min_bt = bt[i]
                idx = i
        if idx == -1:
            t += 1
            continue
        st[idx] = t
        wt[idx] = st[idx] - at[idx]
        t += bt[idx]
        tat[idx] = t - at[idx]
        done[idx] = 1
    total_wt = sum(wt)
    total_tat = sum(tat)
    print("SJF Scheduling ")
    print(f"Process \t AT \t BT \t ST \t WT \t TAT")
    for i in range (n):
        print(f"P{i+1} \t {at[i]} \t {bt[i]} \t {st[i]} \t {wt[i]} \t {tat[i]}")
        
    print(f"Total Wating Time : {total_wt}")
    print(f"Average Wating Time : {total_wt/n}")
    print(f"Total Turn Around Time : {total_tat}")
    print(f"Average Turn Around Time : {total_tat/n}")
    
# Example usage
#sjf([0, 2, 4, 6], [8, 4, 2, 1])
at = [0,1,2,3]
bt = [7,6,5,4]
sjf(at,bt)