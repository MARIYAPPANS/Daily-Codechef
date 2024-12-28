import math
t = int(input())
while t > 0:
    n,x,y= map(int, input().split())
    s=y/30
    print(math.ceil((n+s)/x))
    t -= 1
