t = int(input())
for _ in range(t):
    x, y, z, m = map(int, input().split())
    A = x - z
    B = y - m

    if A == B:
        print("ANY")
    elif A < B:
        print("First")
    else:
        print("Second")
