n=int(input())
arr=list(map(int,input().strip().split()))[:n]
a=int(input())
c=0
for i in range(n):
    if(arr[i]==a):
        c+=1
print(c)
   