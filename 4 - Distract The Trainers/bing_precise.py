def solution(banana_list):
    from fractions import gcd
    from collections import defaultdict

    def lose_game(x, y):
        if (x + y) % 2 == 1:
            return True
        z = x + y
        while z % 2 == 0:
            z /= 2
        return x > z

    def match(banana_list):
        length = len(banana_list)
        match = [-1] * length
        for i in range(length):
            if match[i] == -1:
                for j in range(i + 1, length):
                    if match[j] == -1 and lose_game(banana_list[i], banana_list[j]):
                        match[i] = j
                        match[j] = i
                        break
        return match

    def rematch(banana_list, match):
        length = len(banana_list)
        for i in range(length):
            if match[i] > i:
                for j in range(i + 1, length):
                    if match[j] > j and (match[i] == -1 or lose_game(banana_list[i], banana_list[j])):
                        if match[i] != -1:
                            match[match[i]] = -1
                        if match[j] != -1:
                            match[match[j]] = -1
                        match[i] = j
                        match[j] = i
        return match

    match = match(banana_list)
    rematch = rematch(banana_list, match)

    return len([i for i in rematch if i == -1])


