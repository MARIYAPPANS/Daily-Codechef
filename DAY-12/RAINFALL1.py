# cook your dish here
t=int(input())
while(t):
    x=int(input())
    if x<3:
        print("light")
    elif x>=3 and x<7:
        print("Moderate")
    else:
        print("Heavy")
    t=t-1