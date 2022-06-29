n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(i==0 or i==1):
        c+=1
if(c==n):
    print(True)
else:
    print(False)