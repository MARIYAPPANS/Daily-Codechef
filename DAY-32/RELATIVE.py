t = int(input())
while t > 0:
    n, x= map(int, input().split())
    print((x**2)//(2*n))
    t -= 1
