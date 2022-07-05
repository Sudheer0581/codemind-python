n=int(input())
arr=list(map(int,input().strip().split()))
s=0
t=0
for i in range(n//2):
    s=s+arr[i]
for i in range(n//2,n):
    t=t+arr[i]
print(abs(s-t))

    