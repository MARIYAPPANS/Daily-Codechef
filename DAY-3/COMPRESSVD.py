t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))

    if n == 0:
        print(0)
    else:
        count = 1  # Start with the first element
        for i in range(1, n):
            if a[i] != a[i - 1]:  # Only count if it's different from the previous
                count += 1
        print(count)
    
    t -= 1
