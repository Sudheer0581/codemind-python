n=int(input())
arr=list(map(int,input().strip().split()))[:n]
m=int(input())
f=0
for i in range(n):
    if arr[i]==m:
        f=1
        break
if(f==1):
    print("True")
else:
    print("False")

          
       