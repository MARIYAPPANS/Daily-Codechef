t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    rounds = 0
    while n > 1:
        rounds += 1
        n //= 2
    print((rounds * a) + ((rounds - 1) * b))
