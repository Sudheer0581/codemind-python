n=input()
q=n.split()
l=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in range(len(q)):
    p=len(q[i])
    if(q[i][0] in l and q[i][p-1]):
        c+=1
print(c)