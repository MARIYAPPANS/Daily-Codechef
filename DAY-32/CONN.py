for _ in range(int(input())):
    N = int(input())
    found = False
    for y in range(N // 7 + 1):
        if (N - 7 * y) % 2 == 0:
            found = True
            break
    print("YES" if found else "NO")
