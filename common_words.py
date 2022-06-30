s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
for i in s2:
    if i in s1:
        print(i,end=' ')
