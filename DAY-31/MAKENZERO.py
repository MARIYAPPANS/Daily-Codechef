for _ in range(int(input())):
    n = int(input())
    while n >= 0:
        if n % 3 == 0 or n % 4 == 0:
            print("YES")
            break
        n -= 4
    else:
        print("NO")
