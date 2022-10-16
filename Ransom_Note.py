a=input()
a=a.split()
x=a[0]
y=list(a[1])
c=0
for i in x:
    for j in y:
        if i==str(j):
            c+=1
            y.remove(i)
            break
if c==len(x):
    print(True)
else:
    print(False)