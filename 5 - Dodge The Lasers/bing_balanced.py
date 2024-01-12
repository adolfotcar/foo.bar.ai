from math import floor, sqrt

def solution(str_n):
    n = int(str_n)
    return str(sum([floor(i * sqrt(2)) for i in range(1, n + 1)]))



