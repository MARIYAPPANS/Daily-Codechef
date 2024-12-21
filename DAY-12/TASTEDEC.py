# cook your dish here
t=int(input())

while(t):
    x,y=map(int,input().split())
    if x*2>y*5:
        print("Chocolate")
    elif x*2==y*5:
        print("Either")
    else:
        print("Candy")
    t=t-1