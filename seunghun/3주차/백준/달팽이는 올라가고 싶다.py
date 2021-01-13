import math
import sys

arr = sys.stdin.readline().split(' ')
v = int(arr[2])
a = int(arr[0])
b = int(arr[1])
c = v - a
day = 1
day += math.ceil(c / (a-b))
print(int(day))
