for _ in range(int(input())):
    x, y = map(int, input().split())
    t = 0
    while y < x:
        t += 1
        y += t
    print(t)
