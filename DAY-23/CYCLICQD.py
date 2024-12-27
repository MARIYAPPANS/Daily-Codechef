t = int(input())
while t > 0:
    n,x,y,z= map(int, input().split())
    if n+y==180 and x+z==180:
        print("yes")
    else:
        print("no")
    t -= 1
