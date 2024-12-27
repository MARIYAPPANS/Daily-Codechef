from collections import defaultdict

t =int(input())
while t > 0:
    n=int(input())
    a=list(map(int, input().split()))
    p=defaultdict(int)
    for d, r in enumerate(a, start=1):
        p[r]=max(p[r], d)

    print(sum(p.values()))
    t -= 1
