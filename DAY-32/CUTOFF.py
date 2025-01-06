t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if n==x:
        print(a[0]-1)
    else:
        print(a[-x]-1)