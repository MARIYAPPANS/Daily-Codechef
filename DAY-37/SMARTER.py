import math
t = int(input())
while t > 0:
    n,x,y= map(int, input().split())
    to=(math.ceil(n/x))
    ha=(math.ceil(n/y))
    if to>ha:
        print((to-ha)-1)
    else:
        print(-1)
    t -= 1

