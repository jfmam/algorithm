def findNum(num, st, fin):
    global arr
    mid = (st + fin) // 2 #
    if st > fin:
        return 0
    if arr[mid] < num: #
        return findNum(num, mid+1, fin) #
    elif arr[mid] == num: #
        return 1
    else:
        return findNum(num, st, mid-1)


n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

m = int(input())
ar = list(map(int, input().split(' ')))
for i in ar:
    r = findNum(i, 0, n-1)
    print(r)
