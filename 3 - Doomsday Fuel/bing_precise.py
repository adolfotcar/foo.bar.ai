from fractions import Fraction
from functools import reduce
import numpy as np

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def solution(m):
    # Convert the matrix into fractions
    m = [list(map(Fraction, row)) for row in m]
    
    # Find terminal states
    terminal_states = [i for i, row in enumerate(m) if sum(row) == 0]
    
    # Normalize the matrix
    for i, row in enumerate(m):
        s = sum(row)
        if s > 0:
            m[i] = [v/s for v in row]
    
    # Convert to numpy array for easier manipulation
    m = np.array(m)
    
    # Reorder the matrix to have terminal states first
    order = terminal_states + [i for i in range(len(m)) if i not in terminal_states]
    m = m[:, order][order]
    
    # Separate Q and R matrices
    n = len(terminal_states)
    Q = m[n:, :n]
    R = m[n:, n:]
    
    # Calculate N = (I - R)^-1
    N = np.linalg.inv(np.eye(len(R)) - R)
    
    # Calculate probabilities
    probs = np.matmul(N, np.eye(len(Q[0])))
    
    # Convert to fractions
    probs = [Fraction(x).limit_denominator() for x in probs[0]]
    
    # Find least common multiple of denominators
    denoms = [x.denominator for x in probs]
    lcm_denom = reduce(lcm, denoms)
    
    # Convert to common denominator
    probs = [x * (lcm_denom // x.denominator) for x in probs]
    
    # Return numerators and common denominator
    return [x.numerator for x in probs] + [lcm_denom]



