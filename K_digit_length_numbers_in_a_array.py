n,k=map(int,input().split())
arr=list(map(int,input().strip().split()))[:n]
l=[]
d=0
for i in range(n):
    p=arr[i]
    if(p==0):
        d+=1
    if(p<0):
        p=p*-1
    while(p):
        d+=1
        p=p//10
    l.append(d)
    d=0
q=0
for i in range(n):
    if(l[i]==k):
        q+=1
print(q)