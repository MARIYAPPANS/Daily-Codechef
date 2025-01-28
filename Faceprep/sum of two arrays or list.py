#sum of two arrays or list
''' 
Example:
a=[1,2,3]
b=[1,9]
output:
[1,4,2]
'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=len(a)-1
j=len(b)-1
res=[0]*(max(i,j)+1)
k=len(res)-1
car=0
while i>=0 or j>=0 or car:
    summ=car
    if i>=0:summ+=a[i];i-=1
    if j>=0:summ+=b[j];j-=1
    res[k]=summ%10 
    car=summ//10
    k-=1
print(res)
    
