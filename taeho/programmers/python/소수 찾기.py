def solution(n):
    arr = list(range(2, n + 1))
    count = 0
    for i in arr:
        if i == 0:
            continue
        count += 1
        for j in range(i, n + 1, i):
            if arr[j] == 0:
                continue
            arr[j] = 0
    return count

# 테스트 1 〉	통과 (233.61ms, 46.5MB)
# 테스트 2 〉	통과 (246.55ms, 45.1MB)
# 테스트 3 〉	통과 (237.53ms, 46.1MB)
# 테스트 4 〉	통과 (264.77ms, 45.6MB)