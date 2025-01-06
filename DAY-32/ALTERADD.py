T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    diff = B - A
    if diff % 3 == 0 or diff % 3 == 1:
        print("YES")
    else:
        print("NO")
