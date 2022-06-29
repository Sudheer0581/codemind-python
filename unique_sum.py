n=int(input())
arr=list(map(int,input().strip().split()))
se=set(arr)
s=0
for i in se:
    if arr.count(i)>=1:
        s=s+i
print(s)