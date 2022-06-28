n=input()
q=n.split()
l=['a','e','i','o','u']
c=0
for i in q:
    for j in i:
        if(j in l):
            c+=1
    print(c,end=" ")
    c=0