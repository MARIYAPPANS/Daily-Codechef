t = int(input())
while t > 0:
    x,y,z= map(int, input().split())
    if x+y<z:
        print("PlaneBus")
    elif x+y>z:
        print("Train")
    else:
        print("Equal")
    t -= 1

