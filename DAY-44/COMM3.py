for _ in range(int(input())):
    R = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    d1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
    d3 = (x2 - x3) ** 2 + (y2 - y3) ** 2
    R2 = R ** 2

    if (d1 <= R2 and d2 <= R2) or (d1 <= R2 and d3 <= R2) or (d2 <= R2 and d3 <= R2):
        print("yes")
    else:
        print("no")
