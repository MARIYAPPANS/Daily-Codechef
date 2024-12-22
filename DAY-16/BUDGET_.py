t=int(input())
while(t):
    x,y=map(int,input().split())
    print("yes" if x>=y*30 else "no")
    t=t-1