for _ in range(int(input())):
    n = int(input())
    c=0
    for i in range(1,n+1):
            n-=i
            if n>=0:
                c+=1
            else:
                break
    print(c)
        
