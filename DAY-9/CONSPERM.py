t = int(input())

for _ in range(t):
    n = int(input())
    if (n * (n + 1) / 2) % (n + 1) == 0:
        print(-1)
        continue
    # n is odd here
    lst = [i for i in range(1, n + 1)]
    a = 1
    b = n - 2
    while a < b:
        (lst[a], lst[b]) = (lst[b], lst[a])  # swap
        a += 2
        b -= 2
    for i in lst:
        print(i, end=" ")
    print()
