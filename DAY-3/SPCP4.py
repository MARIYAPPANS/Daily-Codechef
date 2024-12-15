t = int(input())

for _ in range(t):
    ns, nb, nt = map(int, input().split())
    
    # Calculate remaining boys and girls after forming full groups
    remaining_boys = nb % nt
    remaining_girls = (ns - nb) % nt
    
    # Minimize the number of students reading books by pairing boys and girls
    pairs = min(remaining_boys, remaining_girls)
    
    # The remaining students who will read are the leftovers after pairing
    print(remaining_boys + remaining_girls - 2 * pairs)
