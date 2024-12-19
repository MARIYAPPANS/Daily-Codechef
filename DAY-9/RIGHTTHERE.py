# cook your dish here
t=int(input())
while(t):
    x,y=map(int,input().split())
    print("yes" if x<=y else "no")
    t=t-1