for _ in range(int(input())):
    n=int(input())
    aa=list(map(int,input().split()))
    adef=list(map(int,input().split()))
    
    pa=list(map(int,input().split()))
    pdef=list(map(int,input().split()))
    
    if sum(aa)>sum(pa) and sum(adef)>sum(pdef):
        print("A")
    
    elif sum(aa)<sum(pa) and sum(adef)<sum(pdef):
        print("P")
    
    else:
        print("DRAW")
    