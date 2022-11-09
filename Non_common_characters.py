n=input()
n=n.lower()
n=n.split()
m=input()
m=m.lower()
m=m.split()
s11=""
s22=""
for i in n:
    s11+=i
for i in m:
    s22+=i
s1=set(s11)
s2=set(s22)
c=0
for j in s1:
    if j!=" " and j not in s2 :
        #print(j)
        c+=1
for j in s2:
    if j!=" " and j not in s1:
        #print(j)
        c+=1
print(c)