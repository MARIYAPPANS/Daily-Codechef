t = int(input())
while t > 0:
    n, x= map(int, input().split())
    if n>x:
        print("yes")
    else:
        print("no")
    t -= 1
