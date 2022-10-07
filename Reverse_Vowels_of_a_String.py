n=input()
c=[]
k=0
for i in n:
    if i in "aeiouAEIOU":
        c.append(i)
c=c[::-1]
for i in n:
    if i not in "aeiouAEIOU":
        print(i,end="")
    else:
        print(c[k],end="")
        k+=1