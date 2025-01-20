for _ in range(int(input())):
    d, x, y = map(int, input().split())
    if y >= x:
        print(0)
    else:
        s = 0
        while y > 0:
            s += 1
            y -= 1
            p = x * (100 - d * s) / 100
            if y >= p:
                print(s)
                break
        else:
            print(-1)
