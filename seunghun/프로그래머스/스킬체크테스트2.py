def solution(phone_number):
    a = phone_number[0:-4]
    answer = '*' * len(a) + phone_number[-4:]
    return answer
