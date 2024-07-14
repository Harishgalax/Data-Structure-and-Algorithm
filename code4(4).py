def longest_common_subsequence(A, B):
    m, n = len(A), len(B)

    # Create a 2D array to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example usage:
A = "abbcdgf"
B = "bbadcgf"
result = longest_common_subsequence(A, B)
print("The length of the longest common subsequence:", result)
