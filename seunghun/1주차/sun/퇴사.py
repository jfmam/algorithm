# 고려사항
# 기저사례: 퇴사일 수가 넘어가는 날엔 일을 할 수 없다.

def DFS(T, Sum):
    global Max
    if T == n:
        Max = max(Max, Sum)
        return
    else:
        if T + arr[T][0] <= n:
            DFS(T + arr[T][0], Sum + arr[T][1])
        DFS(T+1, Sum)


n = int(input())
arr = []
Max = 0

for i in range(n):
    a, b = input().split(' ')
    arr.append((int(a), int(b)))

DFS(0, 0)
print(Max)
