import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
answer = 0


for i in range (len(arr)-1, 0, -1):
    p = arr[i] - arr[i-1]
    answer = max(p, answer)
    answer += 1

#왕눈이의 위치는 0 부터 시작임으로 -1 일 때도 계산이 필요하다.
answer = max(arr[0], answer)
print(answer)