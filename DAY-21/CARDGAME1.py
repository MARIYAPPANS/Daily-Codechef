t = int(input())
while t > 0:
    n, x = map(int, input().split())
    even_count = n // 2
    odd_count = n - even_count
    
    if x % 2 == 0:
        print(even_count - 1)
    else:
        print(odd_count - 1)
    
    t -= 1
