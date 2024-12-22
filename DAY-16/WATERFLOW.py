t=int(input())
while(t):
    x,y,z,m=map(int,input().split())
    if x+(z*m)>y:
        print("overflow")
    elif x+(z*m)<y:
        print("unfilled")
    else:
        print("filled")
    t=t-1