n, m = input().split(' ')
n = int(n)
m = int(m)
result = 0

arr = list(map(int, input().split(' ')))

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            Sum = arr[i] + arr[j] + arr[k]
            if m < Sum: 
                continue
            ab = m - Sum
            result = max(result, Sum)

print(result)
