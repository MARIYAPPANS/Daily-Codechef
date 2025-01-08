for _ in range(int(input())):
    n, x, k, p = map(int, input().split())
    
    if k == 0:
        print(p)
    else:
        mana_gain = min(k, x) * 10 + max(0, k - x) * 5
        if k == n:
            mana_gain += 20
        print(p + mana_gain)
