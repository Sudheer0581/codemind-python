n=input()
s=''
maxi=0
mini=1000
for i in n:
    if i!=" ":
        s+=i
#print(s)
a=(max(s))
b=(s.count(max(s)))
c=min(s)
d=s.count(min(s))
print(c,d,a,b)
