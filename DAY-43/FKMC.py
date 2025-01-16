for _ in range(int(input())):
    n = int(input())
    s = input()
    
    ones = s.count('1')
    if ones == n or ones == 0:
        print(n)
        continue
    
    max_days = ones
    absents = 0
    for c in s:
        if c == '0':
            absents += 1
            max_days = max(max_days, ones + absents)
        else:
            absents = 0
    
    print(max_days)
