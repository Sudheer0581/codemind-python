n=input()
l=[]
for i in n:
    if i in 'aeiouAEIOU' and i not in l:
        l.append(i)
        print(i,end=" ")
        f=1
if f==0:
    print("-1")