import math

T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    boxes_per_shelf = math.ceil(Y / Z)
    total_boxes = X * boxes_per_shelf
    print(total_boxes)
