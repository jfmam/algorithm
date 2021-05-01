import sys
input = sys.stdin.readline

#입력
# 2
# 3
# 2 2 2
# 2 2 2
# 3
# 1 2 3
# 1 2 1

# 출력
# 8
# 7

T = int(input()) # 테스트 케이스

for _ in range(T):
    n = int(input())
    time = 0
    remaningTime = 0

    microwaveTime = list(map(int, input().split()))
    eatingTime = list(map(int, input().split()))
    total = []

    for i in range(n):
        time += microwaveTime[i]
        total.append((microwaveTime[i], eatingTime[i]))
    
    total.sort(key=lambda x: -1 * x[1])

    for i in range(n):
        remaningTime -= total[i][0]
        remaningTime = max(remaningTime, total[i][1])
    
    time += remaningTime
    print(time)