from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    m=Counter(s)
    c=0
    for i in m.values():
        if i%2!=0:
            c+=1
            break
    print("yes" if c==0 else "no")
    