for _ in range(int(input())):
    r,g,b = map(int, input().split())
    if r+g>=b and g+b>=r and b+r>=g:
        print("yes")
    else:
        print("no")
       
        
        
