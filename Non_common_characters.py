n1=input()
s1=n1.lower()
n2=input()
s2=n2.lower()
l=[]
k=' '
c=0
for i in s1:
    if i not in s2 and i not in k and i not in l:
        l.append(i)
for i in s2:
    if i not in s1 and i not in k and i not in l:
        l.append(i)
print(len(l))
