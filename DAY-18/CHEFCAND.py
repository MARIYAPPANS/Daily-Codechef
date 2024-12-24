t=int(input())
while(t):
    x,y=map(int,input().split())
    if y>=x:
        print(0)
    else:
        s=x-y
        print((s+3)//4)
    t=t-1
