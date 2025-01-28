for i in range(int(input())):
    n,m,r=map(int,input().split())
    l=list(map(int,input().split()))
    res=0
    maxi=0
    mini=0
    for i in l:
        if(m<=i and i<=r):
            res+=1
            maxi=max(maxi,res)
        else:
            res-=1
            mini=min(mini,res)
    print(maxi,mini)