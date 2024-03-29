from itertools import chain


def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n) ]
    row, col = 0, -1
    num = 1
    for i in range(n):
        direction = i % 3
        for j in range(i, n):
            if direction == 0: # direction down
                col += 1
            elif direction == 1: # direction right
                row += 1
            else: # direction up
                col -= 1
                row -= 1
            arr[col][row] =  num
            num += 1
    result = [i for i in chain(*arr) if i != 0]
    return result

# https://programmers.co.kr/learn/courses/4008/lessons/12738 2차원 -> 1차원
