# cook your dish here
for _ in range(int(input())):
    n,x,y = map(int,input().split())
    
    if n>=x:
        print("pizza")
    elif n>=y:
        print("burger")
    else:
        print("nothing")