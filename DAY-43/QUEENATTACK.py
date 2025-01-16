t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    horizontal = n - 1
    vertical = n - 1
    diagonal1 = min(x - 1, y - 1) + min(n - x, n - y)
    diagonal2 = min(x - 1, n - y) + min(n - x, y - 1)
    print(horizontal + vertical + diagonal1 + diagonal2)
