n=int(input())
count=1
f=0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0 and n%i==0:
            f=1
            break
    if f==1:
        count+=1
    f=0
print(count)