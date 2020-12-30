a = int(input())
arr = []
ans = 0

for i in range(a):
    arr = list(map(int, str(i)))
    tmp = i
    for j in arr:
        tmp += j
    if tmp == a:
        ans = i
        break

print(ans)