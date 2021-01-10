numbers = list(map(int, input().split(' ')))

def check(arr, target):
    return not target in arr

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.add(numbers[i] + numbers[j])
    answer.sort()
    return answer

solution(numbers)
