def solution(n):
    if not n or n < 3:
        return 0  # Minimum of 2 steps required, which requires 3 bricks

    # Initialize the memoization table
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty staircase has one possible configuration

    # Fill up the memoization table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, i):
            # Add a step of height 'j' to any staircase of height 'i-j'
            dp[i] += dp[i - j]

    return dp[n]


