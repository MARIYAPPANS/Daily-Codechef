t = int(input())
while t > 0:
    x,y,z= list(map(int, input().split()))
    if x>50:
        print('A')
    elif y>50:
        print('B')
    elif z>50:
        print('C')
    else:
        print("NOTA")
    
    t -= 1
