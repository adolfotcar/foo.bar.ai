def solution(M, F):
    m, f = int(M), int(F)
    generations = 0
    while m != 1 or f != 1:
        if f <= 0 or m <= 0:
            return "impossible"
        if f > m:
            f, m = m, f
        generations += m // f
        m %= f
    return str(generations)


