n=input()
s=input()
f=0
for i in n:
    if i in s and n.count(s)>1:
        print(n.count(s))
        f=1
        break
if f==0:
    print("-1")