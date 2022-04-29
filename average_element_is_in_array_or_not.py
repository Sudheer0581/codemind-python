n=int(input())
s=0
f=0
a=list(map(int,input().strip().split()))[:n]
for  i in range(n):
    s=s+a[i]
c=s//n
for i in range(n):
    if c==a[i]:
         f=1
         break
if f==1:
    print("True")
else:
    print("False")
