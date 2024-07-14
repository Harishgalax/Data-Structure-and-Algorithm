def min_cost_path(cost_matrix, m, n):
    # Create a 2D array to store minimum cost values
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the dp array
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = float('inf')
            elif i == 1 and j == 1:
                dp[i][j] = cost_matrix[i-1][j-1]
            else:
                dp[i][j] = cost_matrix[i-1][j-1] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]

# Example usage:
cost_matrix = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

M, N = 2, 2
result = min_cost_path(cost_matrix, M, N)
print("Minimum cost to reach ({}, {}): {}".format(M, N, result))
