t = int(input())
for _ in range(t):
    if sum(map(int, input().split())) >= 4:
        print("yes")
    else:
        print("no")
