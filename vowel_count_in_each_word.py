n=input()
s=n.split()
l='aeiouAEIOU'
c=0
for i in s:
    for j in i:
        if j in l:
            c+=1
    print(c,end=' ')
    c=0