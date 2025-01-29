def gov_size(cases):
    res = []
    for case in cases:
        n, k, a = case
        cnt = {}
        self = set()

        for i, x in enumerate(a, 1):
            if i == x:
                self.add(x)
            cnt[x] = cnt.get(x, 0) + 1

        sz = 0
        for s, v in cnt.items():
            if v >= k and s not in self:
                sz += 1

        res.append(sz)
    return res


# Read input
T = int(input())
cases = []
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cases.append((n, k, a))

# Compute results
res = gov_size(cases)

# Output results
for r in res:
    print(r)