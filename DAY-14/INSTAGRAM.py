t=int(input())
while(t):
    x,y=map(int,input().split())
    print("no" if y*10>=x else "yes")
    t=t-1