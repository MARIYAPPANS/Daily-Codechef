t=int(input())
while(t):
    x,y=map(int,input().split())
    print(x+(x//10)-(x-y))
    t=t-1