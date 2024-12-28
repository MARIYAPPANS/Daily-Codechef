T = int(input())
for _ in range(T):
    N = int(input())
    if N < 4:
        print(0)  # Not enough ink to form a rectangle
    else:
        side1 = N // 4
        side2 = (N - side1 * 2) // 2
        print(side1 * side2)
