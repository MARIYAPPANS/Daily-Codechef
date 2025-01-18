t = int(input())
while t > 0:
    n = int(input())
    x = list(map(int, input().split()))
    k = int(input())
    init = x[k-1]
    x.sort()
    print(x.index(init)+1)
    t -= 1

