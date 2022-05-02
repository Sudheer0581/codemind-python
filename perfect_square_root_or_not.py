n=int(input())
f=0
for i in range(n):
    if(n==i*i):
       f=1
       break
if(f==1):
    print("True")
else:
    print("False")