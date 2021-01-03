a = int(input())

if(a < 100):
    print(a)
    exit()
cnt=99
for i in range(100, a+1):
    tmp = i
    arr = []
    ch = True
    while tmp != 0:
        arr.append(tmp % 10)
        tmp //= 10
    for i in range(len(arr)-2):
        if(arr[i] - arr[i+1] != arr[i+1] - arr[i+2]):
            ch = False
    if(ch):
        cnt += 1

print(cnt)