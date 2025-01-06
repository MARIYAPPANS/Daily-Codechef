t = int(input())
while t > 0:
    n, x = map(int, input().split())
    while n < x: n *= 2
    while x < n: x *= 2
    print("yes" if n == x else "no")
    t -= 1
