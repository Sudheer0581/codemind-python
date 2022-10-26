a=input()
b=input()
s=''
x=''
for i in a:
    if i!=" ":
        s+=i
for i in b:
    if i!=" ":
        x+=i
s=s.lower()
x=x.lower()
#print(s,x)
l=[]
for i in s:
    if i in x and i not in l:
        l.append(i)
for i in x:
    if i in s and i not in l:
        l.append(i)
v=sorted(l)
if(len(l)==0):
    print("-1")
else:
    for i in v:
        print(i,end="")