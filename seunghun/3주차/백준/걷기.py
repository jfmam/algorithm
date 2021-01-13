import sys

x, y, w, s = sys.stdin.readline().split(' ')
x = int(x)
y = int(y)
w = int(w)
s = int(s)
Min = sys.maxsize


# def dfs(a, b, time):
#     global Min
#     if(a > x or b > y):
#         return
#     if a == x and b == y:
#         Min = min(Min, time)
#     else:
#         dfs(a+1, b, time+w)
#         dfs(a, b+1, time+w)
#         dfs(a+1, b+1, time+s)


# dfs(0, 0, 0)
# print(Min)

# 다른 풀이
if s < 2 * w:
    if x > y:
        x, y = y, x # 어떤 변이 더 긴지 모를 때 그냥 바꿔버린다.
    if s < w:
        if (y - x) % 2 == 0:
            print(x * s + (y - x) * s)
        else:
            print(x * s + (y - x - 1) * s + w) # 대각선으로 이동이 가능 할 때 / \ 둘다 가능하다.
    else:
        print(x * s + (y - x) * w)
else:
    print((x + y) * w)
