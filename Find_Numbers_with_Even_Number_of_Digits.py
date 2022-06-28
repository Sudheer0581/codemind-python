n=int(input())
arr=list(map(int,input().strip().split()))
c=0
for i in range(n):
    l=len(str(arr[i]))
    if l%2==0:
        c+=1
print(c)