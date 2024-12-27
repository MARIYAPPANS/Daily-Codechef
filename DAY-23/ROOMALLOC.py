t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    rooms_needed = 0
    for students in a:
        rooms_needed += (students + 1) // 2  
    print(rooms_needed)
    t -= 1
