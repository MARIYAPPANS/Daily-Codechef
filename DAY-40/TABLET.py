for _ in range(int(input())):
    n, b = map(int, input().split())
    m = 0
    for _ in range(n):
        w, h, p = map(int, input().split())
        if p <= b:
            m = max(m, w * h)
    print(m if m > 0 else "no tablet")
