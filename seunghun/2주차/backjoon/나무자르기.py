def calcSum(ar, k):
    Sum = 0
    for i in ar:
        if i-k > 0:
            Sum += (i-k)
    return Sum


def f(st, fin):
    global maxV
    global m
    global ar
    if(st > fin):
        return
    mid = (st + fin)//2
    Sum = calcSum(ar, mid)
    if Sum >= m:
        maxV = max(maxV, mid)
        return f(mid+1, fin)
    else:
        return f(st, mid-1)


maxV = 0
n, m = input().split(' ')
n = int(n)
m = int(m)
ar = list(map(int, input().split(' ')))
f(0, max(ar))
print(maxV)
