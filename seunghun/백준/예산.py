import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
total = int(input())
Max = max(arr)
Min = 0

if sum(arr) <= total:
    print(Max)
    exit()

ans = -1 * sys.maxsize

while Max >= Min:
    Mid = (Max + Min) // 2
    Sum = 0
    for i in arr:
        if i <= Mid:
            Sum += i
        else:
            Sum += Mid
    if Sum <= total:
        Min = Mid + 1
        ans = max(ans, Mid)
    else:
        Max = Mid - 1

print(ans)