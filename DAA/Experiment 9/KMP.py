def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0
    occurrences = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]
    return occurrences

def main():
    while True:
        print("\n===== KMP String Matching Algorithm =====")
        print("1. Run with default input")
        print("2. Run with custom input")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = "ABABDABACDABABCABAB"
            pattern = "ABABCABAB"
        elif choice == '2':
            text = input("Enter the text string: ")
            pattern = input("Enter the pattern string: ")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        print(f"\nText     : {text}")
        print(f"Pattern  : {pattern}")
        matches = kmp_matcher(text, pattern)

        if matches:
            print("Pattern found at positions:", matches)
        else:
            print("Pattern not found.")

if __name__ == "__main__":
    main()
