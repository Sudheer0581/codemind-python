n=input()
n1=list(n)
l=['a','e','i','o','u']
for i in n1:
    if(i in l):
        l.remove(i)
if(len(l)==0):
    print("0")
else:
    print(*l)