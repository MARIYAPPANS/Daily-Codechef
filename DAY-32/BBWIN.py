for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = (b + 10) - a
    print((diff + 2) // 3 if diff > 0 else 0)
