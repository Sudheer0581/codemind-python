a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
c=0
d=0
for i in range(len(a)):
    if(a[i]>b[i]):
        c+=1
    elif(a[i]<b[i]):
        d+=1
print(c,d)
            