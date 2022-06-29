n=int(input())
arr=list(map(int,input().strip().split()))[:n]
a=int(input())
c=0
for i in range(n):
    p=arr[i]
    if(arr[i]<=a and arr[i]!=1):
        for j in range(2,p//2+1):
            if(p%j==0):
                break
        else:
            c+=1
print(c)