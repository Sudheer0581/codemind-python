a=input()
a=a.split()
j=""
k=""
l=[]
x=""
n=""
for i in a:
    n=""
    x=""
    i=str(i)
    j+="a"
    h=i[0]
    if h in "aeiouAEIOU":
        n=n+i
        n+="ma"
    else:
        for o in range(1,len(i)):
            x+=i[o]
        n+=x
        n+=h
        n+="ma"
    n+=j
    l.append(n)
print(*l)