a=input()
a=a.split(":")
hh=int(a[0])
mm=int(a[1])
if hh>12 and hh<24:
    if(hh-12<=9):
        print("0"+str(hh-12)+":"+a[1]+" "+"PM")
    else:
        print(str(hh-12)+":"+a[1]+" "+"PM")
if hh>0 and hh<12:
    print(a[0]+":"+a[1]+" "+"AM")
if hh==00:
    print("12:00 AM")
if hh==12:
    print("12:00 PM")