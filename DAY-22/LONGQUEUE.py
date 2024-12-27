t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    sushil_wealth = a[-1]
    position = n
    for i in range(n - 2, -1, -1): 
        if a[i] <= sushil_wealth // 2:
            position -= 1
        else:
            break
    print(position)
    t -= 1
