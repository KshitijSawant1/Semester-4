def compute_lps(p):
    lps, length, i = [0]*len(p), 0, 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length-1]
        else:
            i += 1
    return lps

def kmp_search(t, p):
    lps, res, i, j = compute_lps(p), [], 0, 0
    while i < len(t):
        if t[i] == p[j]:
            i += 1
            j += 1
        if j == len(p):
            res.append(i - j)
            j = lps[j - 1]
        elif i < len(t) and t[i] != p[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res

# --- Main ---
text = input("Enter text: ")
pattern = input("Enter pattern: ")

result = kmp_search(text, pattern)
print("\nPattern found at:", result if result else "No match")
