t = int(input())
while t > 0:
    n, x = map(int, input().split())
    income = 2 ** x
    for _ in range(n):
        income //= 2
    print(income)
    t -= 1
