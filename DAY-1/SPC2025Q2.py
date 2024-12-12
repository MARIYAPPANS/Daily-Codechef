# https://www.codechef.com/problems/SPC2025Q2

t=int(input())
while(t):
    nch,ved,var=map(int,input().split())
    ch=list(map(int,input().split()))
    
    if ved+max(ch)>var+(sum(ch)-max(ch)):
        print("ved")
    elif ved+max(ch)==var+(sum(ch)-max(ch)):
        print("Equal")
    else:
        print("Varun")
    t=t-1
    