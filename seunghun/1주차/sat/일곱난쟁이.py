arr = []
for i in range(9):
    arr.append(int(input()))

Sum = sum(arr)

ch1 = 0
ch2 = 0

for i in range(8):
    for j in range(i+1, 9):
        if(Sum - arr[i] - arr[j] == 100):
            ch1 = arr[i]
            ch2 = arr[j]
            break; 

arr.remove(ch1)
arr.remove(ch2)
arr.sort()

for i in arr:
    print(i)
