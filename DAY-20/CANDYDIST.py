t=int(input())
while(t):
    x,y=map(int,input().split())
    if x%y==0 and (x//y)%2==0:
        print("yes")
    else:
        print("no")
    t=t-1
