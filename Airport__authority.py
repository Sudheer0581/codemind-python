n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
x=int(input())
s=0
for i in l:
    if(i>x):
        s=s+2
    else:
        s=s+1

print(s)