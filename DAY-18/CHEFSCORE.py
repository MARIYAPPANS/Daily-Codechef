t=int(input())
while(t>0):
    x,y,z=map(int,input().split())
    if x*y>=z and z%y==0:
        print("yes")
    else:
        print("no")
        
    t-=1
