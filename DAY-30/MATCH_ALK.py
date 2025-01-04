for _ in range(int(input())):
    points=[]
    for _ in range(1,23):
        a,b=list(map(int,input().split()))
        points.append(a*1+b*20)
    maxx=max(points)
    print((points.index(maxx))+1)
        
        