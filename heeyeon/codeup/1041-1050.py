# 1041 - 1050

# 1041 : 문자 입력받아 다음 문자 출력
a=input()
a=ord(a)+1
print(chr(a))

# 1042 : 정수 2개 입력받아 몫 출력
a,b=input().split(" ")
c=int(a)//int(b)
print(c)

# 1043 : 정수 2개 입력받아 나머지 출력
a,b=input().split(" ")
c=int(a)%int(b)
print(c)

# 1044 : 정수 입력받아 다음 수 출력
a=int(input())
print(a+1)

# 1045 : 정수 2개 입력받아 계산 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(a+b,a-b,a*b,a//b,a%b,sep="\n")
print("%.2f" %(a/b))

# 1046 : 정수 3개 입력받아 합, 평균 출력
a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
print(a+b+c)
print("%.1f" %((a+b+c)/3))

# 1047 : 정수 입력받아 2배 출력
a=int(input())
print(a<<1)

# 1048 : 어떤수와 2거듭제곱 곱셈 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(a*(2**b))

# 1049 : 정수 2개 입력받아 비교(우위)
a,b=input().split(" ")
a=int(a)
b=int(b)
print("%d" %(a>b))

# 1050 : 정수 2개 입력받아 비교(동등)
a,b=input().split(" ")
a=int(a)
b=int(b)
print("%d" %(a==b))