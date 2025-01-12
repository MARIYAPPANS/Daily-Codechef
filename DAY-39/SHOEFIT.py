for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a+b+c >=1 and a+b+c <=2:
        print(1)
    else:
        print(0)
