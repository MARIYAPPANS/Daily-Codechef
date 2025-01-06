t = int(input())
while t > 0:
    n, x= map(int, input().split())
    if (n+x)%2==0:
        print("bob")
    else:
        print("alice")
    t -= 1

