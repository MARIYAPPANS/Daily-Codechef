t = int(input())
while t > 0:
    a,x,b,y= map(int, input().split())
    if(a/x)<(b/y):
        print("Bob")
    elif(a/x)>(b/y):
        print("Alice")
    else:
        print("Equal")
    t -= 1

