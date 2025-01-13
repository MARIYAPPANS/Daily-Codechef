T = int(input())
for _ in range(T):
    A, B, C, D, E = map(int, input().split())
    if (A + B <= D and C <= E) or (A + C <= D and B <= E) or (B + C <= D and A <= E):
        print("YES")
    else:
        print("NO")
