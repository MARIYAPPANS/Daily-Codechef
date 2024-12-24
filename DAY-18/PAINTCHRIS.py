# cook your dish here
t=int(input())
while(t):
    x,y,z=map(int,input().split())
    s=x*y 

    if s<=z:
        print((z//2)//s)
    else:
        print(0)
    t=t-1