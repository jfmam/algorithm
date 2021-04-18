# 크게 만들기
import sys
# sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
m = list(input())
stack = []
delK = k

for i in range(n):
    while delK > 0 and stack:
        if stack[-1] < m[i]:
            stack.pop()
            delK -=1
        else:
            break
    stack.append(m[i])

print(''.join(stack[:n-k]))

# DFs 풀이(런타임 에러)

# def DFS(cnt, ans):
#     global Max
#     if(cnt == n - k):
#         Max = max(Max, int(ans))
#         return
#     else:
#         for i in range(n):
#             for j in range(n):
#                 if ch[j] == 0:
#                     ch[j] = 1 
#                     DFS(cnt + 1, ans + m[j])
#                     ch[j] = 0

# DFS(0, '')
# print(Max)
