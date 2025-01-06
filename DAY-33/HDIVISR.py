n=int(input())
maxx=0
for i in range(1,11):
    if n%i==0:
        maxx=max(maxx,i)
print(maxx)
        