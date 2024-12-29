for _ in range(int(input())):
    a,b,x=map(int,input().split())
    if a*b<=x*x:
        print(0)
    elif a*1<=x*x or 1*b<=x*x:
        print(1)
    else:
        print(2)