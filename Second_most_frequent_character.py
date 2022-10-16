n=input()
m=mi=0
max=min=0
total=0
f=0
for i in n:
    if(n.count(i)>max):
        max=n.count(i)
        m=i
for i in n:
    if(n.count(i)<max):
        min=n.count(i)
        mi=i
#print(mi,min)
if(max==1):
    print("-1")
else:
    for i in n:
        if(n.count(i)<max):
            if(n.count(i)>total):
                total=n.count(i)
    for i in n:
        if(n.count(i)==total):
            print(i)
            break