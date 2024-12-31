import math
t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    if a == b:
        print(0)
    elif a < b:
        print(math.ceil((b - a ) / k))
    else:
        print(math.ceil((a - b ) / k))
