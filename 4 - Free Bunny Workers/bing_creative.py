# This function returns the binomial coefficient (n choose k)
def binom(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res *= n - i
        res //= i + 1
    return res

# This function returns a list of lists representing the key distribution
def solution(num_buns, num_required):
    # If only one key is needed, give it to all bunnies
    if num_required == 0:
        return [[] for _ in range(num_buns)]
    # If only one bunny is available, give it all keys
    if num_buns == 1:
        return [[i for i in range(num_required)]]
    # Otherwise, use a recursive formula to generate the distribution
    # based on the observation that each key is shared by (num_buns - num_required + 1) bunnies
    # and each bunny has binom(num_buns - 1, num_required - 1) keys
    distribution = [[] for _ in range(num_buns)]
    start = 0
    for i in range(num_buns - num_required + 1):
        # Get the distribution for the subproblem with one less bunny and one less key
        sub_distribution = solution(num_buns - 1, num_required - 1)
        # Assign the keys to the bunnies according to the subproblem
        for j in range(num_buns - 1):
            distribution[j + i] += [k + start for k in sub_distribution[j]]
        # Update the starting index for the next key
        start += len(sub_distribution[0])
    return distribution


