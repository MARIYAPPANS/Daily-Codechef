t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    valuation1 = a * 10
    valuation2 = b * 5
    if valuation1 > valuation2:
        print("FIRST")
    elif valuation1 < valuation2:
        print("SECOND")
    else:
        print("ANY")
