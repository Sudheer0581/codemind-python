n=int(input())
a=list(map(int,input().strip().split()))
l=[]
k=[]
x=[]
for i in range(1,n+1):
    l.append(i)
for j in a:
    if j>0 and j  in l:
        k.append(j)
for i in l:
    if i not in k:
        x.append(i)
print(x[0])