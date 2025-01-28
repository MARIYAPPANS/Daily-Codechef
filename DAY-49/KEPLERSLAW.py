for _ in range(int(input())):
    a,b,c,d = list(map(int,input().split()))
    
    s = (a**2)/(c**3)
    f = (b**2)/(d**3)
    
    print("yes" if s==f else "no")
