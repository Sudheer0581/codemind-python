n=input()
k=n.lower()
n1=k.split()
m=input()
q=m.lower()
m1=q.split()
c=0
for i in n1:
    for j in m1:
        if i==j:
            c+=1
print(c)
        