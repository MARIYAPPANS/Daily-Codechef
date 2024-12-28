t = int(input())
while t > 0:
    x1, y1, x2, y2 = map(int, input().split())
    alex = (x1**2 + y1**2)**0.5
    bob = (x2**2 + y2**2)**0.5
    if alex > bob:
        print("Alex")
    elif alex < bob:
        print("Bob")
    else:
        print("Equal")
    t -= 1
