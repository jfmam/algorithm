# 1021 - 1030

# 1021 : 단어 1개 입력받아 출력
a=input()
print(a)

# 1023 : 실수 1개 입력받아 나누어 출력
a,b=input().split(".")
print(int(a))
print(int(b))

# 1024 : 단어 1개 입력받아 나누어 출력
a=input()
for i in a:
    print("'%s'" %i)

# 1025 : 정수 1개 입력받아 나누어 출력
n=input()
print(int(n[0])*10000)
print(int(n[1])*1000)
print(int(n[2])*100)
print(int(n[3])*10)
print(int(n[4]))

# 1026 : 시분초 입력받아 분만 출력
a,b,c=input().split(":")
print(int(b))

# 1027 : 년월일 입력받아 다르게 출력
a,b,c=input().split(".")
print("%02d-%02d-%04d" %(int(c),int(b),int(a)))

# 1028 :
a=int(input())
print(a)

# 1029 :
a=float(input())
print("%.11lf" %a)

# 1030 :
a=int(input())
print(a)