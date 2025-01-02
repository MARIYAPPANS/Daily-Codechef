t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    for k in range(2, 100):
        if a % k != 0 and b % k != 0 and c % k != 0:
            print(k)
            break
