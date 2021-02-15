n, kim, im = map(int, input().split())
cnt = 0

while kim !=im:
    kim -= kim // 2
    im -= im // 2
    cnt += 1
print(cnt)
