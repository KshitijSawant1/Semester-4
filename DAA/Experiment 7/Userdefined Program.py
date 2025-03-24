def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS string
    lcs_string = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string = X[i - 1] + lcs_string
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], lcs_string


def menu():
    while True:
        print("\nLongest Common Subsequence (LCS) Menu")
        print("1. User-defined input")
        print("2. Default execution (X = 'AGGTAB', Y = 'GXTXAYB')")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            X = input("Enter the first string: ").strip()
            Y = input("Enter the second string: ").strip()
            length, subsequence = lcs(X, Y)
            print("\n--- LCS Result ---")
            print(f"Length of LCS: {length}")
            print(f"LCS: {subsequence}")

        elif choice == "2":
            X = "AGGTAB"
            Y = "GXTXAYB"
            print(f"\nRunning LCS for default strings:\nX = {X}\nY = {Y}")
            length, subsequence = lcs(X, Y)
            print("\n--- LCS Result ---")
            print(f"Length of LCS: {length}")
            print(f"LCS: {subsequence}")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the menu
menu()
