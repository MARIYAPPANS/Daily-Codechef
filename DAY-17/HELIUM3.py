t=int(input())
while(t):
    x,y,z,m=map(int,input().split())
    s=x*y 
    d=z*m 
    
    if d>=s:
        print("yes")
    else:
        print("no")
    t=t-1