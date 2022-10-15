n1=input()
s1=n1.lower()
n2=input()
s2=n2.lower()
l=[]
v=[]
k=' '
for i in s1:
    if i not in s2 and i not in k and i not in l:
        l.append(i)
for i in s2:
    if i not in s1 and i not in k and i not in l:
        l.append(i)
c=sorted(l)
for i in c:
    print(i,end='')
