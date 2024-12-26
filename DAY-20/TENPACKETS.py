t = int(input())
while t > 0:
    x, y = map(int, input().split())
    cost = min(5 * x, 2 * y + x)
    print(cost)
    t -= 1
