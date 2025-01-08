for _ in range(int(input())):
    n, x = map(int, input().split())
    if x == 0:
        print(0)
    else:
        unrat = 2 * n - x
        print(max(0, x - unrat))
