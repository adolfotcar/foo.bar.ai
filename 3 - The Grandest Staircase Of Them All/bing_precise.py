def solution(n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for last in range(1, n+1):
        for left in range(0, n+1):
            dp[last][left] = dp[last-1][left]
            if left >= last:
                dp[last][left] += dp[last-1][left-last]
    ans = 0
    for i in range(1, n+1):
        ans += dp[i][n-i]
    return ans


