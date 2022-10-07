a=input()
c=0
for i in a:
    if(ord(i)>=65 and ord(i)<=90):
        c+=1
if a[0] in "abcdefghijklmnopqrstuvwxyz":
    c+=1
print(c)