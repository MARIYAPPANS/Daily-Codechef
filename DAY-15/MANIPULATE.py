t=int(input())
while(t):
    x,y=map(int,input().split())
    if x>=y:
        print("YES")
    else:
        print("NO")
    t=t-1