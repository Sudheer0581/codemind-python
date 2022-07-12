n=input()
n1=n.split()
m=input()
m1=m.split()
l=[]
k=[]
c=0
for i in n1:
    if n.count(i)==1:
        l.append(i)
for j in m1:
    if m.count(j)==1:
        k.append(j)
for i in l:
    if i in k:
        c+=1
print(c)