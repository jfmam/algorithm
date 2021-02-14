n = int(input())

arr = [list(map(str, input())) for _ in range(n)]
ans = 0

def check(arr):
    cnt = 0
    for i in range(n):
        cntR= 1 # 자기자신을 포함하기 때문에 1부터 시작
        cntC = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]: # 가로 체크
                cntR += 1
            else:
                cnt = max(cnt, cntR) #가로로 더 긴것 체크
                cntR = 1
            if arr[j][i] == arr[j+1][i]:
                cntC += 1
            else:
                cnt = max(cnt, cntC) # 세로로 더 긴것 체크
                cntC = 1
        cnt = max(cnt, cntR, cntC) # 기존의 것과, 가로,세로 중 더 긴 것 체크, 가로,세로가 초기화가 안 되었을 경우이다.
    return cnt

for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] # 양 옆으로 바꾸기
            ans = max(ans, check(arr)) # 바꾼다음 check함수를 통해 최대값을 추출한다.
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i] # 위아래로 바꾸기
            ans = max(ans, check(arr))
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

print(ans)
