t = int(input())
while t > 0:
    x, n = map(int, input().split())
    if 10 * x <= n <= 12 * x:
        print("yes")
    else:
        print("no")
    t -= 1
