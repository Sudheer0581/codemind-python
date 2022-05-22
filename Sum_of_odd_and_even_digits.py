n=int(input())
arr=list(map(int,input().strip().split()))[:n]
s=0
s1=0
for i in range(n):
    if(i%2==0):
        s=s+arr[i]
    else:
        s1=s1+arr[i]
if(abs(s-s1==0)):
    print('YES')
else:
    print('NO')