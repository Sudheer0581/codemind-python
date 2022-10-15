a=input()
x=""
k=""
i=0
for j in a:
    if j in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        x+=j
x=sorted(x)
for j in a:
    if j not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        k+=j
    else:
        k+=x[i]
        i+=1
print(k)