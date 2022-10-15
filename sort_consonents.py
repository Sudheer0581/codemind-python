a=input()
a=a.split()
n=""
for i in a:
    k=0
    x=""
    i=str(i)
    for j in i:
        if j not in "aeiou":
            x+=j
    x=sorted(x)
    for j in i:
        if j in"aeiou":
            n+=j
        else:
            n+=x[k]
            k+=1
    n+=" "
n=n.split()
print(*n)