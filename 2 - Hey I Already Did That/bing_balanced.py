def solution(n, b):
    k = len(n)
    minionID = []
    while n not in minionID:
        minionID.append(n)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        z = int(x, b) - int(y, b)
        n = format(z, '0' + str(k) + 'X').lower()
    return len(minionID) - minionID.index(n)
