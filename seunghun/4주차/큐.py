import sys

n = int(input())
arr = []
answer = []

for i in range(n):
    b = sys.stdin.readline().split()
    if b[0] == "push":
        arr.append(int(b[1]))
    elif b[0] == "back":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[-1])
    elif b[0] == "front":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[0])
    elif b[0] == "size":
        answer.append(len(arr))
    elif b[0] == "empty":
        if len(arr) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif b[0] == "pop":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[0])
            arr.pop(0)

for i in answer:
    print(i)
