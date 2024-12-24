t=int(input())
while(t):
    x=int(input())
    if x==1:
        print("yes")
    else:
        if (x-1)%2!=0:
            print("yes")
        else:
            print("no")
    t=t-1