for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    s = set(p)
    if any(p.count(i) % i != 0 for i in s):
        print("NO")
    else:
        print("YES")
