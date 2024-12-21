t=int(input())
while(t):
    x,y,z,m=map(int,input().split())
    print(min(x+y,z+m))
    t=t-1
