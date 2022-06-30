n=input()
l=[]
s='aeiou'
f=0
for i in n:
    if i in 'aeiou' and i not in l:
        l.append(i)
for j in s:
    if j not in l:
        print(j,end=' ')
        f=1
if f==0:
    print("0")
