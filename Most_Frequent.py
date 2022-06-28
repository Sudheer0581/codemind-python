n=int(input())
arr=list(map(int,input().strip().split()))
q=set(arr)
l=0
f=0
for i in q:
    if arr.count(i)>l:
        l=arr.count(i)
        f=i
print(f)