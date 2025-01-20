for _ in range(int(input())):
    n, k, av = map(int, input().split())
    nums = list(map(int, input().split()))
    t = n + k
    s = ((av * t) - sum(nums)) / k
    print(int(s) if s > 0 and s.is_integer() else -1)
