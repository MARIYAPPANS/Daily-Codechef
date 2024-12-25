t = int(input())
while t > 0:
    n, x= map(int, input().split())
    print(min(n-x,x))
    t -= 1


