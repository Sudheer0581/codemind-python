a=input()
a=a.split()
x=a[-1]
y=min(x)
if(ord(y)>=65 and ord(y)<=90):
    if y.lower() in x:
        print(y.lower())
    else:
        print(y)
else:
    print(y)