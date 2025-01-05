for _ in range(int(input())):
    n,x,y,a,b=list(map(int,input().split()))
    p=x/a 
    q=y/b 
    if p*n>q*n:
        print("diesel")
    elif  p*n<q*n:
        print("petrol")
    else:
        print("any")
