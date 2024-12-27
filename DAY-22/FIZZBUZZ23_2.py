t = int(input())
while t > 0:
    n, x,y= map(int, input().split())
    total_buns=x*5
    print ((n//total_buns)+y)
    t -= 1

