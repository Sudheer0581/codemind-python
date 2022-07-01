def palin(n):
    q=n[::-1]
    if(n==q):
        return True
    else:
        return False
n=input()
s=n.split()
c=0
for i in s:
    if(palin(i.lower())):
        c+=1
print(c)