def solution(banana_list):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def dfs(u):
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                if match[v] == -1 or dfs(match[v]):
                    match[v] = u
                    return True
        return False

    n = len(banana_list)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(banana_list[i], banana_list[j]) > 1:
                adj[i].append(j)
                adj[j].append(i)

    match = [-1] * n
    ans = n
    for i in range(n):
        vis = [False] * n
        if dfs(i):
            ans -= 1
    return ans


