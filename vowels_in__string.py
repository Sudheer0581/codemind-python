n=input()
l=[]
for i in n:
    if i in 'AEIOUaeiou' and i not in l:
        l.append(i)
        f=1
if(f==1):
    print(*l,end=' ')