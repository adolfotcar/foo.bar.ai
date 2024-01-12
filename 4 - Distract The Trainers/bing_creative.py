# A function to check if two trainers can go into an infinite loop
def can_loop(x, y):
    # If x and y are both odd, they can never have the same number of bananas
    if x % 2 == 1 and y % 2 == 1:
        return True
    # If x and y are both even, they will eventually have the same number of bananas
    if x % 2 == 0 and y % 2 == 0:
        return False
    # Otherwise, we need to check the ratio of x and y
    # If the ratio is a power of 2, they will eventually have the same number of bananas
    # If the ratio is not a power of 2, they can go into an infinite loop
    # We can use bitwise operations to check if the ratio is a power of 2
    ratio = max(x, y) // min(x, y)
    return ratio & (ratio - 1) != 0

# A function to find an augmenting path in the bipartite graph using BFS
def find_path(graph, match, dist, u):
    queue = [u]
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            # If v is not matched or the matched pair of v is not visited
            if match[v] == -1 or (dist[match[v]] == -1 and find_path(graph, match, dist, match[v])):
                # Update the matching and the distance
                match[v] = u
                match[u] = v
                dist[u] = -1
                return True
    # No augmenting path found
    return False

# A function to find the maximum matching in the bipartite graph using Hopcroft-Karp algorithm
def max_match(graph, n):
    # Initialize the matching and the distance arrays
    match = [-1] * n
    dist = [-1] * n
    result = 0
    while True:
        # Find the shortest augmenting paths using BFS
        queue = []
        for u in range(n):
            # If u is not matched, add it to the queue and set its distance to 0
            if match[u] == -1:
                dist[u] = 0
                queue.append(u)
            # Otherwise, set its distance to -1
            else:
                dist[u] = -1
        # If the queue is empty, there are no more augmenting paths
        if not queue:
            break
        # For each node in the queue
        while queue:
            u = queue.pop(0)
            for v in graph[u]:
                # If v is not matched or the matched pair of v is not visited
                if match[v] == -1 or dist[match[v]] == -1:
                    # Update the distance of the matched pair of v
                    dist[match[v]] = dist[u] + 1
                    # Add the matched pair of v to the queue
                    queue.append(match[v])
        # Find the augmenting paths using DFS and update the result
        for u in range(n):
            # If u is not matched and there is an augmenting path from u
            if match[u] == -1 and find_path(graph, match, dist, u):
                # Increment the result
                result += 1
    # Return the result
    return result

# A function to solve the problem
def solution(banana_list):
    # Get the number of trainers
    n = len(banana_list)
    # Build the bipartite graph as an adjacency list
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            # If trainer i and trainer j can go into an infinite loop
            if can_loop(banana_list[i], banana_list[j]):
                # Add an edge between them
                graph[i].append(j)
                graph[j].append(i)
    # Find the maximum matching in the graph
    matching = max_match(graph, n)
    # The minimum number of trainers left is the number of trainers minus twice the matching
    return n - 2 * matching


