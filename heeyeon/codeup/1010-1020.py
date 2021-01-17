# 1010 - 1020

# 1010 : 정수 1개 입력받아 출력
a=int(input())
print(a)
print(type(a))

# 1011 : 문자 1개 입력받아 출력
a=str(input())
print(a)
print(type(a))

# 1012 : 실수 1개 입력받아 출력
a=float(input())
print('%f' % a)
print(type(a))

# 1013 : 정수 2개 입력받아 출력
a, b=input().split()
print(int(a), int(b))

# 1014 : 문자 2개 입력받아 순서 바꿔 출력
a, b=input().split()
print(str(b), str(a))

# 1015 : 실수 1개 입력받아 소수둘째자리까지 출력
a=float(input())
print('%.2f' % a)

# 1017 : 정수 1개 입력받아 3번 출력
a=int(input())
print(a,a,a,sep=" ")

# 1018 : 입력 값 그대로 출력-시간
a,b=input().split(":")
print(a, b, sep=":")

# 1019 : 입력 값 그대로 출력-연월일
y,m,d=input().split(".")
y=int(y)
m=int(m)
d=int(d)
print("%04d.%02d.%02d" % (y , m , d))

# 1020 : 입력 값에서 특정값 빼고 출력
a,b=input().split("-")
print(a+b)