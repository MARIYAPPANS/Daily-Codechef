for testcase in range(int(input())):
    t, l = map(int, input().split())
    if(t > l):
        print(l * 2 + 1)
    else:
        print(-1)