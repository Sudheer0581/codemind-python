n=input()
q=n.split()
l=['a','e','i','o','u']
max=0
c=0
for i in range(len(q)):
    for j in range(len(q[i])):
        if(q[i][j] in l):
            c+=1
    if(c>max):
        max=c
    c=0
print(max)
    