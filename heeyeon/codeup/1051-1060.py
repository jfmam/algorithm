# 1051 - 1060

# 1051 : 정수 2개 입력받아 비교(우위)
a,b=input().split(" ")
a=int(a)
b=int(b)
if a<=b:
    print(1)
else:
    print(0)

#
a,b=input().split(" ")
a=int(a)
b=int(b)
z=int(a<=b)
print(z)

# 1052 : 정수 2개 입력받아 비교(동등)
a,b=input().split(" ")
a=int(a)
b=int(b)
z=int(a!=b)
print(z)

# 1053 : 참 거짓 바꾸어 출력
a=int(input())
b=int(not a)
print(b)

# 1054 : 둘 다 참일 때 참 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(int(a and b))

# 1055 : 하나라도 참일 때 참 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(int(a or b))

# 1056 : 서로 다를 때만 참 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(int((a and not b) or (not a and b)))

# 1057 : 서로 같을 때만 참 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(int((not a and not b) or (a and b)))

# 1058 : 둘 다 거짓일 때만 참 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(int(not a and not b))

# 1059 : 비트 단위로 not하여 출력
a=int(input())
print(~a)

# 1060 : 비트 단위로 and하여 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(a & b)