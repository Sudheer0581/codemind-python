s=input()
s1=s.lower()
x=input()
s2=x.lower()
l=[]
k=' '
c=0
for i in s1:
    if i in s2 and i not in l and i not in k:
        l.append(i)
print(len(l))