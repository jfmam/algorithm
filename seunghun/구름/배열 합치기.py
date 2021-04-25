import sys
input = sys.stdin.readline
n, m = input().split()
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

newArr = arr1 + arr2

for i in sorted(newArr):
    print(i, end=' ')

