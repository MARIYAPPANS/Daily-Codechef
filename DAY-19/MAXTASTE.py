t = int(input())
while t > 0:
    n, x, y ,z= map(int, input().split())
    print(max(x,n)+max(y,z))
  
    t -= 1

