# 1061 - 1070

# 1061 : 비트 단위로 or하여 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(a | b)

# 1062 : 비트 단위로 xor하여 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(a ^ b)

# 1063 : 정수 2개 입력받아 큰 수 출력
a,b=input().split(" ")
a=int(a)
b=int(b)
print(a if a>b else b)

# 1064 : 정수 3개 입력받아 작은 수 출력
a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
print((a if a<b else b) if (a if a<b else b)<c else c)

# 1065 : 정수 3개 입력받아 짝만 출력
a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
if a%2==0: print(a)
if b%2==0: print(b)
if c%2==0: print(c)

# 1066 : 정수 3개 입력받아 짝홀 출력
a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
if a%2==0: print("even")
else: print("odd")
if b%2==0: print("even")
else: print("odd")
if c%2==0: print("even")
else: print("odd")

# 1067 : 정수 1개 입력받아 짝홀 분석
a=int(input())

if a%2==0:
    if a>0: print("plus")
    else: print("minus")
    print("even")
if a%2!=0:
    if a>0: print("plus")
    else: print("minus")
    print("odd")

# 1068 : 정수 1개 입력받아 점수 출력
a=int(input())
if 90<=a<=100: print("A")
elif 70<=a<90: print("B")
elif 40<=a<70: print("C")
elif 0<=a<40: print("D")

# 1069 : 점수 입력받아 평가 출력
a=input()
if a=="A": print("best!!!")
elif a=="B": print("good!!")
elif a=="C": print("run!")
elif a=="D": print("slowly~")
else: print("what?")

# 1070 : 월 입력받아 계절 출력
a=int(input())
if 3<=a<=5: print("spring")
elif 6<=a<=8: print("summer")
elif 9<=a<=11: print("fall")
elif a==1 or a==2 or a==12: print("winter")
else: print("no")