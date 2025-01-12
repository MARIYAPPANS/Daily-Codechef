for _ in range(int(input())):
    n, l, x = map(int, input().split())
    r = n - l
    print(min(l, r) * x)
