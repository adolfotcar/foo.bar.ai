def solution(num_buns, num_required):
    bunnies = [[] for _ in range(num_buns)]
    if num_required == 0:
        return bunnies

    num_copies = num_buns - num_required + 1
    for key in range(num_copies):
        for bunny in range(key, key + num_required):
            bunnies[bunny % num_buns].append(key)

    return bunnies


