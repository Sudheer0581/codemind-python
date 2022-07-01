n=input()
s=set(n)
c=0
for i in s:
    if i in 'aeiou':
        c+=1
if c==5:
    print("True")
else:
    print("False")

