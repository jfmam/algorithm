import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
arr = list(map(int, input().split()))
calc = list(map(int, input().split()))
Min = sys.maxsize
Max = -1 * sys.maxsize


def DFS(Sum, add, minus, multiple, div, idx):
    global Max, Min
    if idx == n:
        Max = max(Max, Sum)
        Min = min(Min, Sum)
    else:
        if add:
            DFS(Sum + arr[idx], add - 1, minus, multiple, div, idx + 1)
        if minus:
            DFS(Sum - arr[idx], add, minus-1, multiple, div, idx + 1)
        if multiple:
            DFS(Sum * arr[idx], add, minus, multiple - 1, div, idx + 1)
        if div:
            DFS(int(Sum / arr[idx]), add, minus, multiple, div-1, idx + 1)


DFS(arr[0], calc[0], calc[1], calc[2], calc[3], 1)
print(Max)
print(Min)
