#Second largest
'''
Example:
a=[1,2,3]
output: 
2 
'''
n = int(input())
nums = list(map(int, input().split()))
lar = -float('inf')
sec = -float('inf')
for i in nums:
    if i > lar:
        sec = lar
        lar = i
    elif i > sec and i != lar:
        sec = i
print(sec)
