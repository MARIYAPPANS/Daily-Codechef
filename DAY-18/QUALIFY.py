t = int(input())
while t > 0:
    x, y, z = map(int, input().split())
    print("Qualify" if x <= (y + (z * 2)) else "NotQualify")
    t -= 1
