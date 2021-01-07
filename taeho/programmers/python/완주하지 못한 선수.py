def solution(participants, completion):
    participants.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participants[i]:
            return participants[i]
    return participants[-1]

