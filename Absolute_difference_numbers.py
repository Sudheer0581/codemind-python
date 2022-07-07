n,m=map(int,input().split())
p=str(n)
l=len(p)
s=0
q=0
for i in range(0,m):
    s=s*10+int(p[i])
for j in range(l-m,l):
    q=q*10+int(p[j])
print(abs(q-s))