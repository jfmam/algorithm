import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
answer = 0


for i in range (len(arr)-1, 0, -1):
    p = arr[i] - arr[i-1]
    answer = max(p, answer)
    answer += 1

answer = max(arr[0], answer)

if answer == p:
    answer += 1
print(answer)