t = int(input())
for _ in range(t):
    items = list(map(int, input().split()))
    print(sum(items)-min(items))