n=int(input())
arr=list(map(int,input().strip().split()))
s=0
p=0
for i in range(n):
    if i%2==0:
        s=s+arr[i]
    else:
        p=p+arr[i]
if(abs(s-p)%4==0):
    print("X")
else:
    print("Y")
    