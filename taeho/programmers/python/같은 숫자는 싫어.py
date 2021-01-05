def solution(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] != arr[i + 1] if i != len(arr) - 1 else arr[i] - 1:
            result.append(arr[i])
    return result


print(solution([1, 1, 3, 3, 0, 1, 1]))
