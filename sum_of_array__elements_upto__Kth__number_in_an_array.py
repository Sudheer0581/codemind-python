n=int(input())
arr=list(map(int,input().strip().split()))
k=int(input())
s=0
for i in range(n):
    if(arr[i]>k):
        break
    else:
        s+=arr[i]
print(s)