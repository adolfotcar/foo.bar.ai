from fractions import Fraction

def solution(pegs):
    n = len(pegs)
    if n < 2:
        return [-1, -1]
    if n == 2:
        a = 2 * (pegs[1] - pegs[0])
        return [a, 3]
    d = pegs[1] - pegs[0]
    for i in range(2, n):
        if (pegs[i] - pegs[i-1]) != d:
            return [-1, -1]
    last_d = pegs[-1] - pegs[-2]
    if n % 2 == 0:
        d = 3 * last_d
    else:
        d = last_d
    a = 2 * (pegs[1] - pegs[0] - d)
    if a < 1:
        return [-1, -1]
    return [a, 1]


