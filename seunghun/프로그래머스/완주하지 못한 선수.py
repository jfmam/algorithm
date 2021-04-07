def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = participant[-1]
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            break

    return answer

# array 다루기
# arr.index("찾으려는 아이템")
# arr.remove("제거하려는 아이템")
# del arr[arr.index('item')] 은 remove와 같은 효과

# 효율성을 위해서는 1중 for문으로 처리 또한 answer를 찾을 시 break 필요