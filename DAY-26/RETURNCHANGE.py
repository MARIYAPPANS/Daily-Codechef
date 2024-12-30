t=int(input())
for _ in range(t):
    x=int(input())
    if x%10<5:
        print(100-((x//10)*10))
    else:
        x=x+5
        print(100-((x//10)*10))
    