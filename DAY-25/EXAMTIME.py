t=int(input())
while(t>0):
    d=list(map(int,input().split()))
    s=list(map(int,input().split()))
    if sum(d)>sum(s):
        print("Dragon")
    elif sum(d)<sum(s):
        print("SLOTH")
    else:
        if d[0]>s[0]:
            print("Dragon")
        elif d[0]<s[0]:
            print("SLOTH")
        else:
            if d[1]>s[1]:
                print("Dragon")
            elif d[1]<s[1]:
                print("SLOTH")
            else:
                print("tie")
    t-=1