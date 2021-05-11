import math


def solution(n, a, b):
    cnt = 1

    if a > b:
        b, a = a, b

    while math.ceil(a/2) != math.ceil(b/2):
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        cnt += 1
    return cnt
