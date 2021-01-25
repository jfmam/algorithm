n = int(input())
arr = []
stack = []
answer = []
count = 1
temp = True

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        answer.append('+')
    if num == stack[-1]:
        answer.append('-')
        stack.pop(-1)
    else:
        temp = False
if not temp:
    print("NO") 
else:
    for i in answer:
        print(i)
