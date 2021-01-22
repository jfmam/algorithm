n, k = map(int, input().split())
num = list(range(1, n+1))
arr = []
i = k-1
while not num:
    arr.append(num.pop(i))
    i = (i+k-1) % len(num)
print('<'+', '.join(arr)+'>')
