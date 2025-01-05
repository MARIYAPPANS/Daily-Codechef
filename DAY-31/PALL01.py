for _ in range(int(input())):
    n=int(input())
    s=str(n)
    d=s[::-1]
    if n==int(d):
        print("wins")
    else:
        print("loses")