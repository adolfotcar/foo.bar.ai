from itertools import combinations

def solution(num_buns, num_required):
    num_keys = num_buns - num_required + 1
    bunnies = [[] for _ in range(num_buns)]
    for i, combination in enumerate(combinations(range(num_buns), num_keys)):
        for j in combination:
            bunnies[j].append(i)
    return bunnies


