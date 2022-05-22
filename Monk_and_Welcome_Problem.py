n=int(input())
arr1=list(map(int,input().strip().split()))[:n]
arr2=list(map(int,input().strip().split()))[:n]
for i in range(n):
    s=arr1[i]+arr2[i]
    print(s,end=" ")