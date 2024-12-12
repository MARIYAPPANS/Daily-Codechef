# cook your dish here
t = int(input())
while t:
    n, k = list(map(int, input().split()))
    
    # Maximum number of 1's in alternating binary string
    max_ones = (n + 1) // 2
    # Minimum number of 1's in alternating binary string
    min_ones = n // 2
    
    # Check if k lies within the valid range
    if k >= min_ones and k <= max_ones:
        print("YES")
    else:
        print("NO")
    
    t = t - 1
