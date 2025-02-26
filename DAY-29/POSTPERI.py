t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    min_diff = float('inf')
    for l in range(1, n + 1):
        for w in range(1, m + 1):
            perimeter = 2 * (l + w)
            diff = abs(perimeter - k)
            min_diff = min(min_diff, diff)
    print(min_diff)
