t = int(input())
while t > 0:
    aim,aex,bim,bex= map(int, input().split())
    print("YES" if ((aim-aex)+(bim-bex))<0 else "no")
    t -= 1

