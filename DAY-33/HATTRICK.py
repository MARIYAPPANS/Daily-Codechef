for _ in range(int(input())):
    x = input().split()
    found = any(x[i] == x[i - 1] == x[i + 1] == 'W' for i in range(1, len(x) - 1))
    print("yes" if found else "no")
