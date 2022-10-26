n=int(input())
arr=list(map(int,input().strip().split()))
k=0
s=0
for i in range(n-1,-1,-1):
    s+=arr[i]*(2**k)
    k+=1
print(s)