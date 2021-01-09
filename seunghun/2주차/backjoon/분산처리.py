import sys

t = int(input())
arr = []

for i in range(t):
    n, m = input().split(' ')
    arr.append((int(n), int(m)))



for i in arr:
    one = []
    c = i[0]
    for j in range(1, i[1]):
        c *= j
        if not c % 10 in one:
            one.append(c)
        else:
            break
    b = i[1] % len(one)
    if b == 0: 
        print(one[len(one) -1])
    else:
        print(one[b -1])

#모범 답안
t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline())

    #불 필요한 연산을 먼저 제거한다.
    if a in [1,5,9]: #or연산자 대신 in 연산자 사용하기
        print(a)
        continue

    result_list = []
    temp = 1
    for _ in range(b):
        temp *= a
        temp %= 10
        if temp in result_list:
            break
        result_list.append(temp)
    idx = b % len(result_list) -1
    result = result_list[idx] # 1,5,9로 인해 정확한 idx를 구하는 것에 애를 먹었다.
    if result == 0:
        print(10)
    else:
        print(result) 