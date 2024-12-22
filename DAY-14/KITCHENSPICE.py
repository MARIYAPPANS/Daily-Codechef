t=int(input())
while(t):
    x=int(input())
    if x<4:
        print("mild")
    elif x>=4 and x<7:
        print("medium")
    else:
        print("hot")
    t=t-1