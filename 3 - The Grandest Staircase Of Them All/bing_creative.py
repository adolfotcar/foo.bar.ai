# A function to count the number of partitions of n into parts that are at least k
def f(n, k, memo):
    # If n is less than k, there are no partitions
    if n < k:
        return 0
    # If n equals k, there is one partition
    if n == k:
        return 1
    # If the result is already computed, return it
    if (n, k) in memo:
        return memo[(n, k)]
    # Otherwise, compute the result recursively and store it in the memo
    result = f(n - k, k + 1, memo) + f(n, k + 1, memo)
    memo[(n, k)] = result
    return result

# A function to solve the problem
def solution(n):
    # Initialize a memo dictionary to store the results of subproblems
    memo = {}
    # Return the number of partitions of n into parts that are at least 2
    return f(n, 2, memo)


