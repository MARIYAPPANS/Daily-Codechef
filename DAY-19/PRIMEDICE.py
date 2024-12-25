import sympy
t = int(input())
while t > 0:
    n, x= map(int, input().split())
    if sympy.isprime(n+x):
        print("Alice")
    else:
        print("Bob")
    t -= 1


