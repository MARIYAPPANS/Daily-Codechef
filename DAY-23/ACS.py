t = int(input())
while t > 0:
    P = int(input())
    y = P // 100
    x = P - 100 * y
    if x >= 0 and x + y <= 10:
        print(x + y)
    else:
        print(-1)
    t -= 1
