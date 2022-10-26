n=input()
n=n.split()
c=0
for i in n:
    i=str(i)
    for j in range(len(i)):
        if(i[j] in "aeiou" and i[len(i)-j-1] not in "aeiou"):
            c+=1
print(c)