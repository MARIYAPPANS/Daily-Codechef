t=int(input())
while(t):
    x,y,z=map(int,input().split())
    if x==y or y>x:
        print(0)
    else:
        print((x-y)*z)
    t=t-1