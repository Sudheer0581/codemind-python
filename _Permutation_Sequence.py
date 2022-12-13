from itertools import permutations
a,b=map(int,input().split())
l=[]
t=[]
for i in range(1,a+1):
    l.append(i)
k=len(l)
p=permutations(l,k)
for i in p:
    t.append(list(i))
s=""
for i in t[b-1]:
    s+=str(i)
print(s)