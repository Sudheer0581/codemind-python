a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
for i in b:
    if i in a:
        print(i,end=' ')