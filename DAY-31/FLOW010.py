for _ in range(int(input())):
    a=input()
    
    if a=='b' or a=='B':
        print("BattleShip")
    elif a=='C' or a=='c':
        print("Cruiser")
    elif a=='D' or a=='d':
        print("Destroyer")
    else:
        print("Frigate")
    