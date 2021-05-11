from collections import deque


def solution(arr, location):
    q = deque([(i, v) for i, v in enumerate(arr)])

    result = 0
    priority = max(q, key=lambda x: x[1])[1]

    while 1:
        pop_item = q.popleft()
        if priority == pop_item[1]:
            result += 1
            if location == pop_item[0]:
                return result
            else:
                priority = max(q, key=lambda x: x[1])[1]
        else:
            q.append(pop_item)
