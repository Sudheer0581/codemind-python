n=int(input())
l=[]
s=0
for i in range(n):
    z=input()
    #print(z)
    c=0
    d=0
    if(z=="++X" or z=="X++"):
        c+=1
        l.append(c)
    elif(z=="--X" or z=="X--"):
        d-=1
        l.append(d)
for i in l:
    s=s+i
print(s)