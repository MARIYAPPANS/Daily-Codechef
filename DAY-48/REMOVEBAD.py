for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    maxc = max(freq.values())
    print(0 if maxc == n else n - maxc)
