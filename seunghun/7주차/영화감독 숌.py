n = int(input())
ans = []
i = 666

while(len(ans) != n):
    num = str(i)
    if "666" in num:
        ans.append(int(num))
    i += 1
print(ans[-1])