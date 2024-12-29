t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    coins_won = (2**(n + 1) - 2**(n - x + 1))
    coins_lost = (2**(n - x + 1) - 2)
    print(coins_won - coins_lost)
