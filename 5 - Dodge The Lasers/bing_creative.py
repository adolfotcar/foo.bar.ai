# A dictionary to store the computed sums
memo = {}

def solution(str_n):
    # Convert the input string to an integer
    n = int(str_n)
    # Call the recursive function and return the result as a string
    return str(sum_of_sequence(n))

def sum_of_sequence(n):
    # Base case: the sum of the first term is the first term itself
    if n == 1:
        return 1
    # Check if the sum for n is already computed and stored
    if n in memo:
        return memo[n]
    # Otherwise, compute the sum using the formula and store it
    r = int(n * 2**0.5) # r = floor(sqrt(2) * n)
    s = r - n # s = floor((sqrt(2) - 1) * n)
    result = n * r - n * (n + 1) // 2 + sum_of_sequence(s)
    memo[n] = result
    return result


