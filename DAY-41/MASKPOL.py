# cook your dish here

for _ in range(int(input())):
    n,x = map(int,input().split())
    un  = n-x
    print(min(x,un))
    
