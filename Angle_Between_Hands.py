x=input()
x=x.split(":")
hh=int(x[0])
mm=int(x[1])
a=abs((30*hh)-(11/2)*mm)
if a<180:
    print(a)
else:
    print(360-a)