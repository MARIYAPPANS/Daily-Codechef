n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(q):
    l, r = map(int, input().split())
    s = sum(a[j] * b[j] for j in range(l-1, r))
    print(s)
