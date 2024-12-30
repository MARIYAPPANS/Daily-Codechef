t = int(input())
for _ in range(t):
    N, K, X, Y = map(int, input().split())
    if X > Y:
        print(K * X + (N - K) * Y)
    else:
        print(N * X)
