for _ in range(int(input())):
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    cost = 0
    for a in A:
        cost += min(a * X, Y)
    print(cost)
