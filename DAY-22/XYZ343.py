t = int(input())
for _ in range(t):
    x,y,z= map(int, input().split())
    count=0
    for i in range(1,x+1):
        if i*y<=z:
            count=count+1
    print(x-count)

    
