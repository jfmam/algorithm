answer = [0, 0]


def DFS(arr, i, j, size):
    base = True
    pivot = arr[i][j]
    for x in range(i, i+size):
        for y in range(j, j+size):
            if pivot != arr[x][y]:
                base = False

    if base:
        answer[pivot] += 1
    else:
        newSize = size // 2
        DFS(arr, i, j, newSize)
        DFS(arr, i+newSize, j ,newSize)
        DFS(arr, i, j+ newSize, newSize)
        DFS(arr, i+ newSize, j+ newSize, newSize)


def solution(arr):
    arrLen = len(arr[0])
    DFS(arr, 0, 0, arrLen)
    return answer


result = solution(ar)
print(result)
