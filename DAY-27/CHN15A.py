t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    print(sum((i + k) % 7 == 0 for i in a))
