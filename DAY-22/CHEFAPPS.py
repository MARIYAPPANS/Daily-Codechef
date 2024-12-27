t = int(input())
while t > 0:
    s, x, y, z = map(int, input().split())
    unused_memory = s - (x + y)

    if unused_memory >= z:
        print(0)
    elif unused_memory + x >= z or unused_memory + y >= z:
        print(1)
    else:
        print(2)

    t -= 1
