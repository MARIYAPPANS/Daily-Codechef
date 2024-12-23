t=int(input())

while(t):
    x,y,z,m=map(int,input().split())
    if x+y+z+m==0:
        print("IN")
    else:
        print("Out")
    t=t-1