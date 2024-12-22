t=int(input())
while(t):
    x,y,z=map(int,input().split())
    
    if x+y<=z:
        print(2)
    elif x<=z:
        print(1)
    else:
        print(0)
    t=t-1