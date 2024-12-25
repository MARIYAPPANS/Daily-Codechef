t = int(input())
while t > 0:
    n, x= map(int, input().split())
    s=n//x 
    if 20>s:
        print(s)
    else:
        print(20)
    t -= 1

