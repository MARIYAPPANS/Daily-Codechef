t=int(input())
while(t):
    x,y,z=map(int,input().split())
    print(max(max(x,y),z)-min(min(x,y),z))
    t=t-1
