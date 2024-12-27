t = int(input())
while t > 0:
    x, y = map(int, input().split())
    floor_x = (x - 1) // 10 + 1  # Floor number for room X
    floor_y = (y - 1) // 10 + 1  # Floor number for room Y
    print(abs(floor_x - floor_y))  # Number of floors Chef needs to travel
    t -= 1
