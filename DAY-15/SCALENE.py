t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    if a!=b and a!=c and b!=a and b!=c and c!=a and c!=b:
        print("yes")
    else:
        print("no")
    t -= 1
