t = int(input())
while t:
    x, y, z = map(int, input().split())
    
    if x*z<y:
        print("yes")
    else:
        print("no")
    
    t -= 1

