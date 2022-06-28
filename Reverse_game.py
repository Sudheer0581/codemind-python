n=int(input())
arr=list(map(int,input().strip().split()))
l=[]
for i in range(n):
    q=str(arr[i])
    r=q[::-1]
    l.append(int(r))
for i in range(n):
    print(l[i],end=' ')