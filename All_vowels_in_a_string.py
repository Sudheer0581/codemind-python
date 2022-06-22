n=input()
l=[]
for i in n:
    if i in 'aeiou' and i not in l :
        l.append(i)
if len(l)==5:
    print("True")
else:
    print("False")
        