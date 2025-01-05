for _ in range(int(input())):
    n,x = map(int, input().split())
    a=list(map(int, input().split()))
    mul=n*x 
    summ=sum(a)
    if mul-summ>0:
        print(mul-summ)
    else:
        print(0)