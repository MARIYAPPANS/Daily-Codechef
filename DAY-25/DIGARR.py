t = int(input())
for _ in range(t):
    d = int(input())
    n = input()
    if int(n) % 5 == 0:
        print("yes")
    elif '0' in n or '5' in n:
        print("yes")
    else:
        print("no")
