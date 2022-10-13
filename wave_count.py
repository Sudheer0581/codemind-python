import math
n=int(input())
a=list(map(int,input().split()))
c=0
x=0
for i in range(1,len(a)-1,2):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        c+=1
    else:
        x+=1
if x==0:
    print(c)
else:
    print("-1")