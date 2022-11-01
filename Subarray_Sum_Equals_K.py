n,k=map(int,input().split())
s=list(map(int,input().strip().split()))
c=0
for i in range(n):
    for j in range(i,n):
        if(sum(s[i:j+1])==k):
            c+=1
print(c)