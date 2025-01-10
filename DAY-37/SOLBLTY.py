t = int(input())
while t > 0:
    x, a, b = map(int, input().split())
    s = 100 - x
    d = a + s * b  # The solubility at 100°C
    print(d * 10)   # Convert to solubility per liter
    t -= 1
