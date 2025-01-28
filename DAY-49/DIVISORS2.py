import sys
import math

MOD = 10**9 + 7

def sieve(n):
    """Generate all prime numbers up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    primes = [p for p, is_prime in enumerate(sieve) if is_prime]
    return primes

def prime_factors(x, primes):
    """Compute the prime factorization of x using the list of primes."""
    factors = {}
    for p in primes:
        if p * p > x:
            break
        while x % p == 0:
            factors[p] = factors.get(p, 0) + 1
            x //= p
    if x > 1:
        factors[x] = 1
    return factors

def count_divisors(factors):
    """Calculate the number of divisors from the prime factorization."""
    result = 1
    for p, exp in factors.items():
        result *= (exp + 1)
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    A = list(map(int, data[2:2+N]))
    
    # Step 1: Compute the prime factorization of M!
    primes = sieve(M)
    m_factorial_factors = {}
    for p in primes:
        count = 0
        n = M
        while n >= p:
            count += n // p
            n //= p
        m_factorial_factors[p] = count
    
    # Step 2: Precompute primes up to the maximum possible A_i
    max_A = max(A)
    primes_A = sieve(max_A)
    
    # Step 3: For each A_i, compute F(B_i)
    results = []
    for a in A:
        # Step 3a: Compute prime factorization of a
        a_factors = prime_factors(a, primes_A)
        
        # Step 3b: Combine factors of a and M!
        combined_factors = a_factors.copy()
        for p, exp in m_factorial_factors.items():
            combined_factors[p] = combined_factors.get(p, 0) + exp
        
        # Step 3c: Calculate the number of divisors
        divisors = count_divisors(combined_factors)
        results.append(divisors % MOD)
    
    # Step 4: Output the results
    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()