
T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    total_slices = N * X
    pizzas = (total_slices + 3) // 4
    print(pizzas)
