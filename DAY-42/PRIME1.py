from sympy import primerange
for _ in range(int(input())):
    s,n=map(int,input().split())
    a=list(primerange(s,n+1))
    
    for i in a:
        print(i)
    print()
