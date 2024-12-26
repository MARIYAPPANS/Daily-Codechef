t = int(input())
while t > 0:
    n, x,y,z= map(int, input().split())
    if n!=y and x!=z:
        print(1)
    else:
        print(2)
    
    t -= 1
