import math
t = int(input())
while t > 0:
    n, x= map(int, input().split())
    if n*100>=x:
        print(0)
    else:
        s=x-(n*100)
        print (int(math.ceil(s/100)))
    t -= 1

