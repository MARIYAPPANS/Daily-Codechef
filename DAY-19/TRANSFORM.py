t = int(input())
while t > 0:
    x = int(input())
    s=x%3
    if s==1:
        print("HUGE")
    elif s==2:
        print("SMALL")
    else:
        print("NORMAL")
    t -= 1


