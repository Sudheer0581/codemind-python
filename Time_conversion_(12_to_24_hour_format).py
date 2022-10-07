a=input()
a=a.split(":")
hh=int(a[0])
x=a[1].split()
mm=int(x[0])
t=x[1]
if t=="PM":
    if hh>=1 and hh<12:
        print(str(12+hh)+":"+x[0])
if hh==12:
    if t=="AM":
        print("00:00")
    else:
        print("12:00")
if t=="AM":
    if hh>=1 and hh<12:
        print(a[0]+":"+x[0])