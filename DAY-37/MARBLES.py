import math
t = int(input())
while t > 0:
    n, x= map(int, input().split())
    print(math.comb(n-1,x-1))
    t -= 1
