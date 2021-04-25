import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
arr = list(map(int, input().split()))
calc = list(map(int, input().split()))
Min = sys.maxsize
Max = -1 * sys.maxsize


def DFS(Sum, calcArr, idx):
    global Max, Min
    if idx == n:
        Max = max(Max, Sum)
        Min = min(Min, Sum)
    else:
        if calcArr[0]:
            calcArr[0] -= 1
            DFS(Sum + arr[idx],calcArr, idx + 1)
            calcArr[0] += 1
        if calcArr[1]:
            calcArr[1] -= 1
            DFS(Sum - arr[idx], calcArr, idx + 1)
            calcArr[1] += 1
        if calcArr[2]:
            calcArr[2] -= 1
            DFS(Sum * arr[idx], calcArr, idx + 1)
            calcArr[2] += 1
        if calcArr[3]:
            calcArr[3] -= 1
            DFS(int(Sum / arr[idx]), calcArr, idx + 1)
            calcArr[3] += 1

b = copy.deepcopy(calc)
DFS(arr[0], b, 1)
print(Max)
print(Min)
