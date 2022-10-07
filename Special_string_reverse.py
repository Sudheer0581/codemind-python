a=input()
x=""
y=""
z=0
for i in a:
    if i in "abcdefghijklmnopqrstuvwxyz":
        x+=i
x=x[::-1]
for i in range(len(a)):
    if a[i] not  in "abcdefghijklmnopqrstuvwxyz":
        y+=a[i]
    else:
        y+=x[z]
        z+=1
print(y)