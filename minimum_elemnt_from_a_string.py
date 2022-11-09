n=input()
k=n.split()
s=[]
for i in k[-1]:
    if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
        s.append(i)
s.sort()
if(s[0].isupper()):
    if(s[0].lower() in s):
        print(s[0].lower())
    else:
        print(s[0])
else:
    print(s[0])