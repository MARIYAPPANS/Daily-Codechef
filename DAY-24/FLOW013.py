T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    if A > 0 and B > 0 and C > 0 and A + B + C == 180:
        print("YES")
    else:
        print("NO")
