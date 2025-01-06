while True:
    n = int(input())
    if n == 0:
        break
    p = list(map(int, input().split()))
    inv = [0] * n
    for i in range(n):
        inv[p[i] - 1] = i + 1
    print("ambiguous" if inv == p else "not ambiguous")
