t=int(input())
while(t):
    x,y=map(int,input().split())
    print(min(x*3,y*2))
    t=t-1