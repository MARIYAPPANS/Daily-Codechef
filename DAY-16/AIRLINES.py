t=int(input())
while(t):
    x,y,z=map(int,input().split())
    seat=x*10
    if seat>=y:
        print(y*z)
    else:
        print((seat)*z)
        
    t=t-1