def calcSum(ar, k):
    arr = []
    for i in ar:
        if i-k > 0:
            arr.append(i-k)
    return sum(arr)


def f(num, st, fin):
    global maxV
    global m
    global ar
    if(st > fin):
        return
    mid = (st + fin)//2
    Sum = calcSum(ar, mid)
    if Sum > m:
        return f(num, mid+1, fin)
    elif Sum == m:
        maxV = max(maxV, mid)
        return f(num, mid+1, fin)
    else:
        return f(num, st, mid-1)


maxV = 0
n, m = input().split(' ')
n = int(n)
m = int(m)
ar = list(map(int, input().split(' ')))
f(n, 0, max(ar))
print(maxV)
