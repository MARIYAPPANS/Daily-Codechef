t=int(input())
while(t):
    x,y=map(int,input().split())
    print("yes" if x*5>=y else "no")
    t=t-1
