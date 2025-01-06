T = int(input())
for _ in range(T):
    x,y,z,m,n,o = map(int, input().split())
    
    if y>=x and m>=z and n>=o:
        print("yes")
    else:
        print("no")
    
