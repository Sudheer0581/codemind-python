n=input()
n=n.lower()
m=input()
m=m.lower()
str1=""
str2=""
l=[]
for i in n:
    str1=str1+i
for i in m:
    str2=str2+i
for i in str1:
    if i in str2:
        l.append(i)
k=set(l)
z=list(k)
q=(sorted(z))
if len(q)==0:
    print("-1")
else:
    for i in q:
        if i!=" ":
            print(i,end='')
