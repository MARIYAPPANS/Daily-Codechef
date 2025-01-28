#string compression
'''
s="aabbac"
output:a2b2ac
'''
s=input()
res=""
c=1 
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1 
    else:
        res+=s[i-1]+(str(c) if c>1 else "")
        c=1 # reset to one for all the var 
res+=s[-1]+(str(c) if c>1 else "")
print(res)    