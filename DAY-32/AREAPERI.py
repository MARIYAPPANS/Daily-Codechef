l=int(input())
b=int(input())

area=l*b 
peri=2*(l+b)

if area>peri:
    print("area")
    print(area)
elif area<peri:
    print("Peri")
    print(peri)
else:
    print("eq")
    print(area)
