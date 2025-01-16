t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    odd_n = (n + 1) // 2
    odd_x = (x + 1) // 2
    print(odd_n * odd_x)
