t = int(input())
while t > 0:
    n, x= list(map(int, input().split()))
    print(max(n,x),n+x)
    t -= 1

