n=input()
q=n.lower()
l=[]
for i in q:
    if i.isalpha() and q.count(i)==1:
        l.append(i)
l.sort()
for i in l:
    print(i,end="")