a=input()
a=a.split()
k=""
p=0
for i in a:
    i=str(i)
    n=""
    p=0
    for j in i:
        if j in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            n+=j
    n=sorted(n)
    for j in i:
        if j not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            k+=j
        else:
            k+=n[p]
            p+=1
    k+=" "
k=k.split()
print(*k)