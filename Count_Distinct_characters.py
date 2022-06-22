n=input()
n1=n.lower()
s=''
for i in n1:
    if i not in s and ord(i)!=32:
        s=s+i
k=list(s)
k.sort()
print(len(k))