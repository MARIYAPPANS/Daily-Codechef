t = int(input())
while t > 0:
    n = int(input())
    x = list(map(int, input().split()))
    
    c = 0
    for i in range(1,n):
        c+=abs(x[i-1]-x[i])-1
    print(c)
    
    t -= 1


