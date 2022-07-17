n=int(input())
arr=list(map(int,input().strip().split()))
rev=0
l=[]
for j in arr:
    while(j):
        r=j%10
        rev=rev*10+r
        j=j//10
    l.append(rev)
    rev=0
    
print(*l)