import sys
x, y, w, h = map(int, sys.stdin.readline().split(' '))
mx = w - x
my = h - y
xmin = min(mx, x)
ymin = min(my, y)
min_value = min(xmin, ymin)

print(min_value)
