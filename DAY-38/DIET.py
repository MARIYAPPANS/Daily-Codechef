t = int(input())
while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    pro = 0
    flag = 0
    for i in range(n):
        if a[i] + pro >= x:
            pro = pro + (a[i] - x)
        else:
            flag = 1
            print("NO", i + 1)
            break
    if flag == 0:
        print("YES")
    t -= 1
