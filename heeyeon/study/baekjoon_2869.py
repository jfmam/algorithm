# 1주차-2

# 달팽이

# a:올라가는 거리 b:미끄러지는 거리 v:나무막대 높이

a,b,v=map(int,input().split(" "))

res=(v-a)/(a-b)
if (v-a)%(a-b) == 0:
    print(int(res+1))
else:
    print(int(res+2))