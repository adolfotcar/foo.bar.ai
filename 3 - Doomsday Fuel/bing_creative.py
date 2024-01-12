# A function to find the greatest common divisor of two numbers
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# A function to simplify a fraction
def simplify(n, d):
    g = gcd(n, d)
    return n // g, d // g

# A function to add two fractions
def add_frac(n1, d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return simplify(n, d)

# A function to multiply two fractions
def mul_frac(n1, d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return simplify(n, d)

# A function to find the probabilities of each terminal state
def solution(m):
    # Find the terminal states and the non-terminal states
    terminal = []
    non_terminal = []
    for i in range(len(m)):
        if sum(m[i]) == 0:
            terminal.append(i)
        else:
            non_terminal.append(i)

    # If the initial state is terminal, return [1, 1]
    if 0 in terminal:
        return [1, 1]

    # Convert the matrix to a list of fractions
    frac = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[i])):
            if sum(m[i]) == 0:
                row.append((0, 1)) # zero fraction
            else:
                row.append(simplify(m[i][j], sum(m[i]))) # simplified fraction
        frac.append(row)

    # Create the identity matrix of the same size as m
    identity = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[i])):
            if i == j:
                row.append((1, 1)) # one fraction
            else:
                row.append((0, 1)) # zero fraction
        identity.append(row)

    # Subtract the non-terminal submatrix from the identity submatrix
    sub = []
    for i in range(len(non_terminal)):
        row = []
        for j in range(len(non_terminal)):
            n, d = identity[i][j]
            n1, d1 = frac[non_terminal[i]][non_terminal[j]]
            n -= n1 * d
            d *= d1
            row.append(simplify(n, d))
        sub.append(row)

    # Find the inverse of the submatrix using Gauss-Jordan elimination
    inv = []
    for i in range(len(sub)):
        inv.append(identity[i] + sub[i]) # augment the matrix

    for i in range(len(inv)):
        # Make the pivot element one
        n, d = inv[i][i]
        for j in range(len(inv[i])):
            inv[i][j] = mul_frac(inv[i][j][0], inv[i][j][1], d, n)
        # Make the other elements in the column zero
        for j in range(len(inv)):
            if i != j:
                n, d = inv[j][i]
                for k in range(len(inv[j])):
                    n1, d1 = inv[i][k]
                    n2, d2 = inv[j][k]
                    n2, d2 = mul_frac(n2, d2, d, 1)
                    n1, d1 = mul_frac(n1, d1, n, 1)
                    n2 -= n1
                    inv[j][k] = simplify(n2, d2)

    # Extract the inverse submatrix
    inverse = []
    for i in range(len(inv)):
        row = []
        for j in range(len(inv[i]) // 2, len(inv[i])):
            row.append(inv[i][j])
        inverse.append(row)

    # Multiply the inverse submatrix with the terminal submatrix
    result = []
    for i in range(len(inverse)):
        row = []
        for j in range(len(terminal)):
            n, d = 0, 1
            for k in range(len(non_terminal)):
                n1, d1 = inverse[i][k]
                n2, d2 = frac[non_terminal[k]][terminal[j]]
                n3, d3 = mul_frac(n1, d1, n2, d2)
                n, d = add_frac(n, d, n3, d3)
            row.append((n, d))
        result.append(row)

    # Find the common denominator of the first row
    denom = 1
    for i in range(len(result[0])):
        denom *= result[0][i][1]
        denom //= gcd(denom, result[0][i][1])

    # Convert the fractions to the common denominator and extract the numerators
    numer = []
    for i in range(len(result[0])):
        numer.append(result[0][i][0] * denom // result[0][i][1])

    # Append the denominator to the answer
    answer = numer + [denom]

    return answer


