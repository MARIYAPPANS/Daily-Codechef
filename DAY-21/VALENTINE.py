t = int(input())
while t > 0:
    n, x = map(int, input().split())
    if n<x:
        print(0)
    else:
        print(n//x)
    t -= 1
