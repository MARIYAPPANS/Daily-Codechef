t=int(input())
while(t):
    x,y,z=map(int,input().split())
    if x>=10 and y>=10 and z>=10 and x+y+z>=100:
        print("pass")
    else:
        print("fail")
    t=t-1
