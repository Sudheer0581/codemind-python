a=input()
b=input()
r=a.lower()
q=b.lower()
x=set(r)
z=set(q)
q=list(x)
v=list(z)
c=0
for i in q:
    if i in v:
        v.remove(i)
        c+=1
if(c==len(q)):
    print("True")
else:
    print("False")