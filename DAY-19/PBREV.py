t = int(input())
while t > 0:
    x = int(input())
    n= map(int, input().split())
    c=0
    for i in n:
        if i>4:
            pass
        else:
            c=c+1
    if c==0:
        print("yes")
    else:
        print("no")
    t -= 1

