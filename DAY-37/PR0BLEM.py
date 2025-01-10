for _ in range(int(input())):
    n, m = map(int, input().split())
    print("YES" if abs(m - n) % 2 == 0 else "NO")
