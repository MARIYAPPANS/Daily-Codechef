t=int(input())
while(t):
    x,y=map(int,input().split())
    
    if (y*6*6)>=x:
        print("yes")
    else:
        print("no")
  
    t=t-1
