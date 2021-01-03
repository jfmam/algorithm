def getLocation(number, target):
    location = {1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    result = abs(location[target][0] - location[number][0]) + \
                 abs(location[target][1] - location[number][1])
    return result


def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        else:
            Ldis = getLocation(left, i)
            Rdis = getLocation(right, i)
            if Ldis<Rdis:
                left = i
                answer += 'L'
            elif Ldis > Rdis:
                right = i
                answer += 'R'
            else:
                if hand == "right":
                    right = i
                    answer += 'R'
                else:
                    left = i
                    answer += 'L'
    return answer
