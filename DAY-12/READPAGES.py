t=int(input())
while(t):
    x,y,z=map(int,input().split())
    print("yes" if y*z>=x else "no")
    t=t-1

