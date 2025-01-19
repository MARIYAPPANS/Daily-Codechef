for _ in range(int(input())):
    n, x = map(int, input().split())
    s = input()
    sw = 0
    v = True
    for c in s:
        if c == '1':
            sw = x
        else:
            sw -= 1
            if sw < 0:
                v = False
                break
    print("YES" if v else "NO")
