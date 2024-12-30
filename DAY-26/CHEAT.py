t = int(input())
for _ in range(t):
    n = int(input())
    print(n // 7 + (1 if n % 7 >= 2 else 0))
