n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,n):
    if(arr[i]==1 or arr[i]==0):
        c+=1
if(len(arr)==c):
    print("True")
else:
    print("False")