t = int(input())
while t > 0:
    x,y,z = map(int, input().split())
    if y-x==z-y:
        print(0)
    else:
        print(1)
    
    t -= 1

