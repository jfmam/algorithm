def checktr(time, arr):
    c = 0
    start = time
    end = time+1000
    for i in arr:
        if i[1] >= start and i[0] < end:
            c += 1
    return c


def solution(lines):
    arr = []
    answer = 1
    for line in lines:
        y, a, b = line.split()
        a = a.split(':')
        b = float(b.replace('s', ''))*1000
        end = (int(a[0])*3600 + int(a[1])*60 + float(a[2]))*1000
        start = end-b+1
        arr.append([start, end])
    for i in arr:
        answer = max(r, checktr(i[0], arr), checktr(i[1], arr))
    return answer
