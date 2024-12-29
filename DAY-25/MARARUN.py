t = int(input())
for _ in range(t):
    D, d, A, B, C = map(int, input().split())
    total_distance = D * d
    
    if total_distance >= 42:
        print(C)
    elif total_distance >= 21:
        print(B)
    elif total_distance >= 10:
        print(A)
    else:
        print(0)
