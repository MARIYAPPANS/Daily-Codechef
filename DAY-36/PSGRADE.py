for _ in range(int(input())):
    a,b,c,tmin,asc,bsc,csc=list(map(int,input().split()))
    if a<=asc and b<=bsc and c<=csc and asc+bsc+csc>=tmin:
        print("yes")
    else:
        print("no")
        
