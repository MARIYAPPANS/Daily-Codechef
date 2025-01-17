for _ in range(int(input())):
    n, x, s = map(int, input().split())
    current = x
    for _ in range(s):
        a, b = map(int, input().split())
        if current == a:
            current = b
        elif current == b:
            current = a
    print(current)
