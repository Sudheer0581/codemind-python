n=input()
n=n.lower()
n=n.split()
s1=""
s2=""
for i in n:
    for j in i:
        if j not in "aeiou":
            s1=s1+j
    k=sorted(s1)
    x=0
    s2=""
    for c in i:
        if c not in "aeiou":
            s2=s2+k[x]
            x=x+1
        else:
            s2=s2+c
    print(s2,end=" ")       
    s1=