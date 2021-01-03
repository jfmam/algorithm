a = int(input())
# solve 1
arr1 = []
for i in str(a):
    arr1.append(i)
print(arr1)

# solve 2
arr2 = []
while(a != 0):
    arr2.append(a % 10)
    # 이 부분을 조심해야한다. c++ 처럼 a/=10으로 작성 할 경우 소수점까지 모두 출력 하기 때문에 몫만 나올 수 있게 작성 해야한다.
    a //= 10
print(arr2)
# solve 3
arr3 = list(map(int, '100'))
print(arr3)

# map은 iter 형시임으로 list를 이용하여 배열 형으로 만들어 준다.
# javascript에선 from 함수와 같다.
