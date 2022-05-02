n=int(input())
q=str(n)
m=int(q[0])
for i in range(1,len(q)):
    if(int(q[i])>m):
        m=int(q[i])
print(m)