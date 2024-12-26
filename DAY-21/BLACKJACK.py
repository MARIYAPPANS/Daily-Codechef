t = int(input())
while t > 0:
    n, x = map(int, input().split())
    target = 21 - n - x
    if 1 <= target <= 10:  # Check if `i` is in the range 1 to 10
        print(target)
    else:
        print(-1)
    t -= 1
