s=input()
n=int(s)
l=[]
k=[]
while(n!=0):
    r=int(n)%10
    l.append(r)
    n=n//10
for i in l:
    if i%2!=0:
        x=i**2
        k.append(x)
    else:
        continue
z1=k[::-1]
z=str(z1)
q=""
for i in z:
    if i!="," and i!= " " and i!="[" and i!="]":
        q=q+i
print(q)