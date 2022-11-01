n=int(input())
m=int(input())
l=[]
c=0
for i in range(n,m+1):
    l.append(i)
for i in range(len(l)):
    for j in range(i,len(l)):
        if(sum(l[i:j+1])%2!=0):
            c+=1
print(c)