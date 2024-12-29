T = int(input())
for _ in range(T):
    N = int(input()) 
    coins = (N // 5) * 4 + (N % 5)
    print(coins)
