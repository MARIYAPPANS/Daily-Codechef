t=int(input())
while(t>0):
    x=int(input())
    if x%2==0:
        print(x//2,x)
    else:
        print((x//2)+1,x)
    t=t-1
