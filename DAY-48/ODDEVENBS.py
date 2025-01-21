testcase_no=int(input())
for testcases in range(testcase_no):
    n = int(input())
    l = list(map(int,input().split()))
    if(n%2==sum(l)%2):
        print("yes")
    else:
        print("no")