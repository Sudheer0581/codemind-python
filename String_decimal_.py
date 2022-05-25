n=int(input())
c=0
for i in range(n):
    m=input()
    for i in m:
        if i in '1234567890':
            c+=1
    if(c==len(m)):
        print(True)
    else:
        print(False)
    c=0