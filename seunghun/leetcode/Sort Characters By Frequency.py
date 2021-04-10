from  collections import Counter

s = input().strip('"')
ans = ""
cnts = Counter(list(s)).most_common()

for item in cnts:
    ans += item[0] * item[1]
print(ans)