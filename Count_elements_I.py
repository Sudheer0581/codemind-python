n,m=map(int,input().split())
arr=list(map(int,input().split()))[:n]
l=list(map(int,input().split()))[:m]
q1=set(arr)
q2=set(l)
c=0
if(n>=m):
    for i in q1:
        for j in q2:
            if(i==j):
                #print(i)
                c+=1
                break
else:
    for i in q2:
        for j in q1:
            if(i==j):
                c+=1
                break
print(c)