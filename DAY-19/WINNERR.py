t = int(input())
while t > 0:
    n, x, y ,z= map(int, input().split())
    if max(x,n)<max(y,z):
        print("P")
    elif max(x,n)>max(y,z):
        print("Q")
    else:
        print("Tie")
    t -= 1

