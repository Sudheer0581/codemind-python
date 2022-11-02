n=input()            #This is Samples
k=n.lower()
c=0
p=len(k)
for i in range(len(k)//2):
    if (k[i] in "aeiou" and k[(p-1)-i] in "bcdfghjklmnpqrstvwxyz")or(k[i] in "bcdfjklmnpqrstvwxyzgh" and k[(p-1)-i] in "aeiou"):
        c+=1
print(c)


