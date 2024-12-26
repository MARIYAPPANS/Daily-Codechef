t = int(input())
while t > 0:
    n, x = map(int, input().split())
    if n == x:
        print(0)
    else:
        # Calculate the difference and check the number of steps
        steps = (x - n + 7) // 8  # Using integer division to calculate steps
        print(steps)
    t -= 1
