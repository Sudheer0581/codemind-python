n1=input()
n2=input()
q1=n1.lower()
q2=n2.lower()
s1=q1.split()
s2=q2.split()
c=0
for i in s1:
    for j in s2:
        if i==j:
            c+=1
print(c)