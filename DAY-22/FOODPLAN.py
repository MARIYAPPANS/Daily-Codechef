t = int(input())
while t > 0:
    n, x= map(int, input().split())
    if (n-(n*0.1))<x:
        print("online")
    elif (n-(n*0.1))>x:
        print("Dining")
    else:
        print("either")
    t -= 1

