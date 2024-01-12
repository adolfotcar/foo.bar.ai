from fractions import Fraction
from numpy import linalg

def solution(m):
    # Convert the matrix to a canonical form
    q, r = linalg.qr(m)
    q_t = q.transpose()
    canonical = q_t.dot(m).dot(q)

    # Split the matrix into Q and R
    q_matrix = q_t.transpose()
    r_matrix = canonical[:len(q), :len(q)]

    # Calculate the fundamental matrix (N)
    n_matrix = linalg.inv((np.identity(len(q)) - r_matrix))

    # Calculate the probability of reaching each terminal state
    terminal_probabilities = []
    for i in range(len(q)):
        terminal_probabilities.append(Fraction(n_matrix[i].sum(), n_matrix.sum()))

    # Return the result
    return [int(x) for x in terminal_probabilities] + [int(n_matrix.sum())]


