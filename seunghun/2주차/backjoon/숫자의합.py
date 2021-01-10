n = int(input())
m = int(input())
Sum = 0
tmp = m
for i in range(n):
    Sum += tmp % 10
    tmp //= 10

print(Sum)
