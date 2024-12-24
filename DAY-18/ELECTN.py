t = int(input())
while t > 0:
    x, y= map(int, input().split())
    z= map(int, input().split())
    c=0
    for i in z:
        if i>=y:
            c+=1
    print(c)
    
    t -= 1
