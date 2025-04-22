def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a DP table of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # characters match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # take max of top or left

    # Reconstruct the LCS from the DP table
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_str))


# ---------- Main Program ----------
X = input("Enter first string: ")
Y = input("Enter second string: ")

length, sequence = lcs(X, Y)
print(f"\nLength of LCS: {length}")
print(f"LCS: {sequence}")
