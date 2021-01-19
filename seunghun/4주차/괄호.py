n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for i in arr:
    left = 0
    right = 0
    Bool = True
    for j in range(len(i)):
        if left < right:
            Bool =False
            break
        if i[j] == '(':
            left += 1
        else:
            right += 1
    if left != right or not Bool:
        print("NO")
    else:
        print("YES")

