t = int(input())
while t > 0:
    x = int(input())
    n = list(map(int, input().split()))
    maxx = 0
    for i in n:
        maxx = max(maxx,n.count(i))
    print(x-maxx)
    t -= 1

