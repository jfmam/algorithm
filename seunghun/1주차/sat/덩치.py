arr = []
n = int(input())
cnt = [1] * n

for i in range(n):
    a, b = input().split(' ')
    arr.append((int(a), int(b)))

for i in range(n):
    for j in range(n):
        if(arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]):
            cnt[i] += 1

for i in cnt:
    print(i)

