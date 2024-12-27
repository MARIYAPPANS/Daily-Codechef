t = int(input())
while t > 0:
    intemp, ans, hot, cold = map(int, input().split())
    if intemp < ans:
        print("yes" if intemp + hot >= ans else "NO")
    elif intemp > ans:
        print("yes" if intemp - cold <= ans else "NO")
    else:
        print("yes")
    t -= 1
