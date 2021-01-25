import sys

n = int(input())
arr = []
answer = []

for i in range(n):
    b = sys.stdin.readline().split()
    if b[0] == "push_back":
        arr.append(int(b[1]))
    elif b[0] == "push_front":
        arr.insert(0, int(b[1]))
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
    elif b[0] == "pop_front":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[0])
            arr.pop(0)
    elif b[0] == "pop_back":
        if len(arr) == 0:
            answer.append(-1)
        else:
            answer.append(arr[-1])
            arr.pop(-1)

for i in answer:
    print(i)
