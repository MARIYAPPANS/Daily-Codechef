for _ in range(int(input())):
    n = int(input())
    s  = input()
    nin = s.count('Y')
    ind = s.count('I')
    if nin>ind:
        print("NOT INDIAN ")
    elif ind>nin:
        print("INDIAN")
    else:
        print("NOT SURE")
 
