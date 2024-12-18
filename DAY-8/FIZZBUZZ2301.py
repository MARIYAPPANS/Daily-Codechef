# cook your dish here
a,b,c=map(int,input().split())
if max(max(a,b),c)==a:
    print("yes")
else:
    print("no")