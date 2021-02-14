import sys
# nCr 구하기
n, r = map(int, sys.stdin.readline().split())
ch= [0] * n

def dfs(s, L):
    if r==L:
        for i in range(L):
            print(ch[i])
    else:
        for j in range(s, n):
            ch[j]
            dfs(j+1, L+1)
dfs(0,0)