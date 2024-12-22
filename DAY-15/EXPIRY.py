t=int(input())
while(t):
    x,y,z=map(int,input().split())
    print("yes" if z*y>=x else "no")
    t=t-1
