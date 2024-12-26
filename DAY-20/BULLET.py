t = int(input())
while t > 0:
    n, x, y= map(int, input().split())
    s=x//n 
    if s<=y:
        print(y-s)
    else:
        print(0)
    t -= 1


