for _ in range(int(input())):
    d,x,y,z=list(map(int,input().split()))
    f=x*7
    s=(y*d)+(z*(7-d))
    print(max(f,s))
