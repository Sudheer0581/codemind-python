'''n=int(input())
l=list(map(int,input().strip().split()))
c=0
k=0
for i in range(n):
    if l[i]==1:
        c+=1
        if(i==n-1):
            if(c>k):
                k=c
    elif(l[i]==0):
        if(c>k):
            k=c
        c=0
print(k)'''
n=int(input())#1 2 3 4 
l=list(map(int,input().split())) # 1 1 0 1 1 1 
p=[]
c=0
mx=0
for i in range(0,n):
    if l[i]==1:
        c=c+1
        if l[i]==l[n-1]:
            p.append(c)
    elif l[i]==0:
        p.append(c)
        c=0
print(max(p))
        