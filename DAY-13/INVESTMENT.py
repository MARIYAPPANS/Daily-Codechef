t=int(input())
while(t):
    x,y=map(int,input().split())
    print("yes" if y*2<=x else "no")
    t=t-1
