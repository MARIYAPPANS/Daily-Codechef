t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    max_strips = max(a, b, c)
    total_strips = a + b + c
    if max_strips <= total_strips - max_strips + 1:
        print("YES")
    else:
        print("NO")
