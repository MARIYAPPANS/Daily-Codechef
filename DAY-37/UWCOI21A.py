for _ in range(int(input())):
    n = int(input())
    found = False
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            print(i, j)
            found = True
            break
