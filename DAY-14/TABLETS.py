t=int(input())
while(t):
    x,y=map(int,input().split())
    print("yes" if y>=x*3 else "no")
    t=t-1