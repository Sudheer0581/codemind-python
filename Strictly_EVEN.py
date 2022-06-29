n=int(input())
arr=list(map(int,input().split()))
c=0
count=0
for i in range(n):
    if(arr[i]%2==0 and i%2==0):
        c+=1
for i in range(n):
    if(arr[i]%2==0):
        count+=1
if(c==count):
    print(True)
else:
    print(False)