for _ in range(int(input())):
    s = input()
    s1 = s[0]
    for i in s[1:]:
        if s1[-1] != i:
            s1 += i
    print(min(s1.count("U"), s1.count("D")))
