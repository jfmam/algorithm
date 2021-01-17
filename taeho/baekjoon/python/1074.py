N, r, c = map(int, input().split())


def zFunc(s, x, y):
    s //= 2
    if s == 0:
        return 0
    for i in range(2):
        for j in range(2):
            if x < s * (i + 1) and y < s * (j + 1):
                return (i * 2 + j) * s * s + zFunc(s, x - s * i, y - s * j)


print(zFunc(2 ** N, r, c))
