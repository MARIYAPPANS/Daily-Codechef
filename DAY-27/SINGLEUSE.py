t = int(input())
for _ in range(t):
    h, x, y = map(int, input().split())
    if y >= h:
        print(1)
    else:
        remaining_health = h - y
        normal_attacks = (remaining_health + x - 1) // x
        print(1 + normal_attacks)
