def solve():
    t = int(input())
    
    for _ in range(t):
        N = int(input())
        
        # Initialize the counts for even and odd divisors
        f_N = 0
        g_N = 0
        
        # Find divisors of N
        for i in range(1, N + 1):
            if N % i == 0:
                if i % 2 == 0:  # Even divisor
                    f_N += 1
                else:  # Odd divisor
                    g_N += 1
        
        # Compare and print the result
        if f_N > g_N:
            print(1)
        elif f_N == g_N:
            print(0)
        else:
            print(-1)

# Call the solve function to execute the code
solve()
