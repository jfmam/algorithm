# 1주차-1

# 손익분기점

# a:고정비용 b:가변비용 c:노트북 가격

a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)

if c<=b: print(-1)
else: print(a//(c-b)+1)