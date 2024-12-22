t=int(input())
while(t):
    x,y=map(int,input().split())
    
    if x<=y:
        print("yes" if x+200>=y else "no")
    else:
        print("no")
    t=t-1
