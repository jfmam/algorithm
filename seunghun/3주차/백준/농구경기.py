n = int(input())
arr = []
ar = set()
ans = []

for i in range(n):
    arr.append(input()[0:1])
    ar.add(arr[i])

for i in list(ar):
    cnt = 0
    for j in arr:
        if i == j:
            cnt += 1
    if(cnt >= 5):
        ans.append(i)

if(len(ans) == 0):
    print("PREDAJA")

ans.sort()
a = ''
for i in ans:
    a += i
print(a)
