n=input()
a=n.lower()
c=0
d=""
for i in a:
    if i!=' ':
        if a.count(i)==1:
            d=d+i
e=(sorted(d))
for i in e:
    print(i,end="")