t=int(input())
while(t):
    x,y,z=map(int,input().split())
    
    if x==y and y==z and x==z:
        print("no")
    else:
        new1=x+y
        new2=x+z 
        new3=y+z 
        
        if z>new1 or y>new2 or x>new3:
            print("yes")
        else:
            print("no")
    t=t-1