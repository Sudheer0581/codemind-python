n=int(input())
arr=list(map(int,input().strip().split()))
m=int(input())
f=0
for i in range(len(arr)):
    if m==arr[i]:
        print(i)
        f=1
if f==0:
    print("-1")