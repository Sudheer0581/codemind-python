n=input()
c=0
for i in n:
    if(i.islower() or i.isupper() or i.isdigit() or i==" "):
        c+=1
print(len(n)-c)