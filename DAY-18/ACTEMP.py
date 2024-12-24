t=int(input())
while(t):
    x,y,z=map(int,input().split())
    
    if y>=x and y>=z:
        print("yes")
    else:
        print("no")
    t=t-1
