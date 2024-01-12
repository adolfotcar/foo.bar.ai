def solution(n, b):
    # Convert n to an integer and store its length
    n = int(n, b)
    k = len(str(n))
    # Initialize an empty list to store the seen minion IDs
    seen = []
    # Repeat until n is already in seen
    while n not in seen:
        # Sort the digits of n in ascending and descending order
        y = "".join(sorted(str(n), reverse=False))
        x = "".join(sorted(str(n), reverse=True))
        # Convert x and y to integers in base b and subtract them
        z = int(x, b) - int(y, b)
        # Convert z to a string in base b and pad it with zeros
        z = format(z, "0" + str(k) + "x")
        # Assign n to z and append it to seen
        n = int(z, b)
        seen.append(n)
    # Find the index of n in seen and subtract it from the length of seen
    cycle_length = len(seen) - seen.index(n)
    # Return the cycle length as an integer
    return cycle_length