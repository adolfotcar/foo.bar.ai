def solution(n):
    # Initialize a 2D array to store the number of staircases that can be built with i bricks and j steps
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # Base case: there is only one way to build a staircase with 0 or 1 step
    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][1] = 1
    # Fill the rest of the table using dynamic programming
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            # If the number of bricks is less than the number of steps, there is no way to build a staircase
            if i < j:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j - 1]
    # The answer is the sum of the number of staircases that can be built with i bricks and j steps for 2 <= j <= n
    ans = 0
    for j in range(2, n + 1):
        ans += dp[n][j]
    return ans


