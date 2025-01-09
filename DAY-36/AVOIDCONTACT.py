t = int(input())
while t > 0:
    x,y= map(int, input().split())
    if x==y:
        print((y*2)-1)
    else:
        print((y*2)+(x-y))
    t -= 1

