n = 1

while True:
    s = input()  # 문자열로 받을 때에는 개행을 제거하기 위해 그냥 input 사용
    arr = []
    cnt = 0
    if s[0] == '-':
        break
    for i in s:
        if len(arr) == 0:
            arr.append(i)
        else:
            if arr[-1] == '{' and i == "}":
                arr.pop()  # 아무것도 안 넣어야 마지막 원소 제거
            else:
                arr.append(i)
    for i in range(0, len(arr), 2):
        if arr[i] == arr[i+1]:
            cnt += 1
        else:
            cnt += 2
    ans = "{n}. {cnt}".format(n=n, cnt=cnt)
    print(ans)
    n += 1
