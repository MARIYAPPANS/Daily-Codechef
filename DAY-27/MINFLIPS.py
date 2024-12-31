t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    if n % 2 != 0:
        print(-1)
    else:
        neg_count = x.count(-1)
        pos_count = x.count(1)
        required_changes = abs(neg_count - pos_count) // 2
        print(required_changes)
