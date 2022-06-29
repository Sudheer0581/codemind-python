n=int(input())
arr=list(map(int,input().strip().split()))
a,b=map(int,input().split())
l=[]
s=0
for i in range(n):
    if arr[i]<a or arr[i]>b:
        l.append(arr[i])
print(sum(l))