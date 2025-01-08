for _ in range(int(input())):
    totb = int(input())
    runs = list(map(int, input().split()))
    c = 0
    summ = 0
    for i in range(len(runs)):
        summ += runs[i]
        if summ == (i + 1):
            c += 1
    print(c)
