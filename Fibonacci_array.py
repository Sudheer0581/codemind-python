n=int(input())
a=list(map(int,input().strip().split()))
c=0
for i in range(n-3):
    if(a[i+2]==a[i]+a[i+1]):
        c+=1
if(c==(n-3)):
    print("yes")
else:
    print("no")