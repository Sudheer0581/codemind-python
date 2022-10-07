a=input()
c=0
maxx=0
for i in a:
    if i in "aeiou":
        c+=1
        maxx=max(c,maxx)
    else:
        c=0
print(maxx)