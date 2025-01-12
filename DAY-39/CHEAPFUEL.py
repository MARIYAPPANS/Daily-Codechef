for _ in range(int(input())):
    x, y, a, b, k = map(int, input().split())
    p = x + a * k
    d = y + b * k
    print("petrol" if p < d else "diesel" if d < p else "same price")
