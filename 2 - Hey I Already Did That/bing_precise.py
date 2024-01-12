def solution(n, b):
    k = len(n)
    history = []

    while n not in history:
        history.append(n)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        z = int(x, b) - int(y, b)
        n = format(z, 'x' if b == 16 else 'd').zfill(k)

    return len(history) - history.index(n)

