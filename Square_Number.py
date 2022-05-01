n=int(input())
f=0
for i in range(n//2):
    for j in range((i+1),(n//2+1)):
        if(n==(i*i)+(j*j)//2):
            f=1
            break
if(f==1):
    print("True")
else:
    print("False")