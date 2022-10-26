a=input()
#print(a)
b=input()
#print(b)
l=[]
s=[]
x=[]
if(a!=b):
    for i in a:
        l.append(i)
    for i in b:
        s.append(i)
    for i in l:
        if i in s:
            x.append(i)
else:
    print("False")
if(len(s)==len(a)):
    print("True")
else:
    print("False")