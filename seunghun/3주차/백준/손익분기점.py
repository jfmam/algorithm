import sys

arr = sys.stdin.readline().split(' ')
if(int(arr[2]) <= int(arr[1])):
    print(-1)
else:
    print(int(arr[0]) // (int(arr[2]) - int(arr[1]))+1)
