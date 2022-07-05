n=int(input())
arr=list(map(int,input().strip().split()))
s=0
q=0
for i in range(n//2):
    s=s+arr[i]
for i in range(n//2,n):
    q=q+arr[i]
print(s)
print(q)