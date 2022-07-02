s1=input()
s2=input()
q1=s1.split()
q2=s2.split()
l=[]
x=[]
for i in q1:
    if q1.count(i)==1:
        l.append(i)
for i in q2:
    if q2.count(i)==1:
        x.append(i)
c=0
for i in l:
    for j in x:
        if i==j:
            c+=1
print(c)