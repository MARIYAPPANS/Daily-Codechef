t=int(input())
while(t):
    x,y=map(int,input().split())
    if x>0 and y>0:
        print("yes" if x==y else "no")
    else:
        print("no")
    t=t-1