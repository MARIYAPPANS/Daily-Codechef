t = int(input())
while t > 0:
    n, x = map(int, input().split())
    nx=x+1
    print(n-(n//nx)*x)
    t -= 1
