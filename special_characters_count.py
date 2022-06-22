n=input()
c=0
for i in n:
    if i not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
        c+=1
print(c)