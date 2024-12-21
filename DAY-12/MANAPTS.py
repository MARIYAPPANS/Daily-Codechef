# cook your dish here
t=int(input())

while(t):
    x,y=map(int,input().split())
    if x>y:
        print(0)
    elif x==y:
        print(1)
    else:
        print(y//x)
    t=t-1