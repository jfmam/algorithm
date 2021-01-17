# 1031 - 1040

# 1031 : 10진수 입력받아 8진수 출력
a=input()
print("%o" %int(a))

# 1032 : 10진수 입력받아 16진수 출력(소)
a=input()
print("%x" %int(a))

# 1033 : 10진수 입력받아 16진수 출력(대)
a=input()
print("%X" %oct(a))

# 1034 : 8진수 입력받아 10진수 출력
a=input()
n=int(a,8)
print("%d" %n)

# 1035 : 16진수 입력받아 8진수 출력
a=input()
n=int(a,16)
print("%o" %n)

# 1036 : 영문자 입력받아 10진수 출력
a=ord(input())
print("%d" %a)

# 1037 : 정수 입력받아 아스키 출력
a=int(input())
print("%s" %chr(a))

# 1038 : 정수 2개 입력받아 합 출력
a,b=input().split(" ")
print(int(a)+int(b))

# 1039 : 정수 2개 입력받아 합 출력
a,b=input().split(" ")
print("%d" %(int(a)+int(b)))

# 1040 : 정수 입력받아 부호바꿔 출력
a=int(input())
print("%d" %(-a))