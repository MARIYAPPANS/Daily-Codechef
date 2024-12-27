t = int(input())
while t > 0:
    n,a,b= map(int, input().split())
    even=n//2
    odd=n-even
    print((a*even)+(b*odd))
    
    t -= 1

