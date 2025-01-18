for _ in range(int(input())):
    s = input()
    c = 0
    for i in s:
        if i in "ADOPRQ":
            c+=1
        if i in "B":
            c+=2
    print(c)
            