t=int(input())
while(t>0):
    x=int(input())
    fact=1 
    for i in range(1,x+1):
        fact*=i 
    print(fact)
    t=t-1
