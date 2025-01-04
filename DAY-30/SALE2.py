for _ in range(int(input())):
    n, x = map(int, input().split())
    print((n - n // 3) * x)
