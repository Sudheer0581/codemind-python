def palin(n):
    q=n[::-1]
    if(n==q):
        return True
    else:
        return False
s=input()
h=s.split()
c=0
for i in h:
    if(palin(i.lower())):
        c+=1
print(c)