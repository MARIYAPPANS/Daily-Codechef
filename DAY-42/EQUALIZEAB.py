t = int(input())
while t > 0:
    x, y, m = map(int, input().split())
    if (x - y) % (2 * m) == 0:
        print("yes")
    else:
        print("no")
    t -= 1
