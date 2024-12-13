ele = list(map(int, input().split()))

elesort = sorted(set(ele))

if len(elesort) > 1:
    print(elesort[-2])
else:
    print(-1)

""" 
1.Sorted makes more easy than traversing through list
2.Set is used Remove the duplicates
3.'if' is used to check a len is greater than one element is present or not
4.if yes print last element's before element
5.else print -1

"""
