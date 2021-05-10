import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    a = [False] * 26
    s = input()
    ch = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            continue
        if a[ord(s[i])-97]:
            ch = True
            break
        a[ord(s[i])-97] = True
    if not ch:
        cnt += 1

print(cnt)
