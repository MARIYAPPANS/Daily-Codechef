t = int(input())
while t > 0:
    n, x = map(int, input().split())
    if n%2==0 or x%2!=0:
        print("yes")
    else:
        print("no")
    t -= 1

