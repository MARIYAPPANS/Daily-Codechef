t = int(input())
while t:
    x, y, z = map(int, input().split())
    if x <= y:
        print(z)
    else:
        if x % y == 0:
            print((x // y) * z)
        else:
            print(((x // y) + 1) * z)
    t -= 1
